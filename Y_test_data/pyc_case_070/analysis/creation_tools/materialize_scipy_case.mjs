import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const specPath = process.argv[2];
if (!specPath) throw new Error("usage: node materialize_scipy_case.mjs <spec.json>");
const spec = JSON.parse(await fs.readFile(specPath, "utf8"));
if (spec.validationStatus && spec.validationStatus !== "verified_base_gold") {
  throw new Error("Base/Gold validation must pass before formal materialization");
}
for (const key of ["verifiedError", "targetSummary"]) {
  if (!spec[key]) throw new Error(`Missing verified evidence field: ${key}`);
}
if (spec.probeEvidenceRoot) {
  const readProbe = async label => JSON.parse(await fs.readFile(
    `${spec.probeEvidenceRoot}/case${spec.caseNumber}-probe-${label}${spec.probeSuffixes?.[label] ?? spec.probeSuffix ?? ""}/summary.json`, "utf8"));
  const baseProbe = await readProbe("base");
  const goldProbe = await readProbe("gold");
  if (baseProbe.exitCode !== (spec.expectedBaseExitCode ?? 139) || goldProbe.exitCode !== 0 || baseProbe.error || goldProbe.error) {
    throw new Error("Recorded Base failure / Gold success evidence does not match the specification");
  }
  for (const [label, expected] of [["base", "FAILED"], ["gold", "PASSED"]]) {
    const log = await fs.readFile(`${spec.probeEvidenceRoot}/case${spec.caseNumber}-probe-${label}${spec.probeSuffixes?.[label] ?? spec.probeSuffix ?? ""}/stdout.raw.log`, "utf8");
    for (const node of [...spec.failToPass, ...spec.passToPass]) {
      const status = spec.passToPass.includes(node) ? "PASSED" : expected;
      if (spec.expectedBaseExitCode === 1 && !log.split("\n").some(line => line.startsWith(node + " ") && line.includes(status))) {
        throw new Error(`Unverified probe node: ${label} ${node}`);
      }
    }
  }
}
const interpreter = spec.pythonExecutable ?? "python3.8";
const project = spec.projectName ?? "SciPy";
const testFiles = spec.testFiles ?? [spec.testFile];
const root = "E:/CLB_Swe-bench";
const repoRoot = `${root}/pyc-swebench`;
const template = `${repoRoot}/Y_test_data/pyc_case_002`;
const caseDir = `${repoRoot}/Y_test_data/pyc_case_${spec.caseNumber}`;
const workbookOnly = process.argv.includes("--workbook-only");
const sourceValues = JSON.parse(await fs.readFile(`${root}/_work/pyc_batch/source_values.json`, "utf8"));
const rows = Array.isArray(sourceValues)
  ? sourceValues.find(x => x.sheet === "analysis result").values
  : sourceValues.values;
const row = rows.find(x => String(x[0]) === String(spec.sourceCase));
if (!row) throw new Error(`source row ${spec.sourceCase} not found`);
if (!String(row[1]).includes(spec.fixCommit)) throw new Error("source row commit mismatch");

const dirs = [
  "analysis/source_material", "patches", "official_swebench", "verification/controls",
  "verification/builds", "verification/runs", "evaluator/image",
];
if (!workbookOnly) {
for (const rel of dirs) await fs.mkdir(path.join(caseDir, rel), { recursive: true });
if (spec.probeEvidenceRoot) {
  for (const label of ["base", "gold"]) await fs.cp(
    `${spec.probeEvidenceRoot}/case${spec.caseNumber}-probe-${label}${spec.probeSuffixes?.[label] ?? spec.probeSuffix ?? ""}`,
    `${caseDir}/verification/probes/${label}`, { recursive: true });
}

await fs.copyFile(`${template}/.gitattributes`, `${caseDir}/.gitattributes`);
for (const name of [
  "build_model_evaluator.ps1", "build_model_evaluator.py", "evaluate_model_patch.ps1",
  "evaluate_model_patch.py", "logging_v3.py", "LOGGING.md", "run_evaluation.sh",
]) await fs.copyFile(`${template}/evaluator/${name}`, `${caseDir}/evaluator/${name}`);
if (spec.nativeAuditCommand) {
  const builderPath = `${caseDir}/evaluator/build_model_evaluator.py`;
  const builder = await fs.readFile(builderPath, 'utf8');
  await fs.writeFile(builderPath, builder.replace('python -c "import numpy; print(numpy.__version__)"', spec.nativeAuditCommand));
} else if (project === 'Pillow') {
  const builderPath = `${caseDir}/evaluator/build_model_evaluator.py`;
  const builder = await fs.readFile(builderPath, 'utf8');
  await fs.writeFile(builderPath, builder.replace('python -c "import numpy; print(numpy.__version__)"',
    `python -c "import PIL; from PIL import Image; print(PIL.${spec.pillowVersionAttribute ?? '__version__'}, Image.core.__file__); assert PIL.${spec.pillowVersionAttribute ?? '__version__'} == Image.core.PILLOW_VERSION == '${spec.version}'"`));
}
for (const asset of spec.additionalRuntimeAssets ?? []) {
  await fs.copyFile(asset.sourcePath, path.join(caseDir, asset.source));
}
if (spec.pytestPathPrefix) {
  const evaluatorPath = `${caseDir}/evaluator/evaluate_model_patch.py`;
  let evaluator = await fs.readFile(evaluatorPath, "utf8");
  evaluator = evaluator.replace("(?P<test_id>scipy/", `(?P<test_id>${spec.pytestPathPrefix}`);
  evaluator = evaluator.replace("    for source, target in runtime_assets:", "    command.extend(config.get(\"docker_run_args\", []))\n    for source, target in runtime_assets:");
  await fs.writeFile(evaluatorPath, evaluator);
}
await fs.copyFile(`${template}/evaluator/image/.dockerignore`, `${caseDir}/evaluator/image/.dockerignore`);
await fs.copyFile(spec.goldPatchSource, `${caseDir}/patches/gold_patch.diff`);
await fs.copyFile(spec.testPatchSource, `${caseDir}/patches/test_patch.diff`);
}

const clean = value => String(value ?? "").replace(/\s+/g, " ").trim();
const locationTypes = [row[4], row[5], row[6]].map(clean).filter(Boolean).join(" + ");
const source = {
  instance_id: spec.sourceInstanceId,
  source_project: "Dissecting Real-World Cross-Language Bugs",
  source_case: String(spec.sourceCase),
  duplicate_source_cases: spec.duplicateSourceCases ?? [],
  deduplication_key: spec.fixCommit,
  language_pair: "Python-C",
  repo: spec.repo,
  issue_id: spec.issueId,
  issue_url: spec.issueUrl,
  commit: spec.fixCommit,
  base_commit: spec.baseCommit,
  base_commit_status: spec.baseCommitStatus ?? "verified_first_parent_of_merge",
  fix_commit: spec.fixCommit,
  commit_url: `https://github.com/${spec.repo}/commit/${spec.fixCommit}`,
  problem_statement: spec.problemStatement,
  symptom: clean(row[2]),
  bug_location: clean(row[3]),
  bug_location_type: locationTypes,
  bug_path: clean(row[7]),
  cross_language_type: clean(row[8]),
  data_control_flow_direction: clean(row[9]),
  root_cause: clean(row[10]),
  fixing_strategy: clean(row[11]),
  fix_location: clean(row[12]),
  trace: {
    available: true,
    upstream_source: spec.issueUrl,
    upstream_description: spec.upstreamDescription,
    verified_error: spec.verifiedError,
    verified_test: spec.verifiedTest,
  },
  evidence_type: spec.evidenceType ?? "source_row_upstream_pr_and_verified_pytest_trace",
  ...(spec.testScope ? { official_test_scope: spec.testScope } : {}),
  runtime_verified: true,
  reproduction_status: "verified_base_fail_gold_pass_docker",
  FAIL_TO_PASS: spec.failToPass,
  PASS_TO_PASS: spec.passToPass,
  gold_patch: "see patches/gold_patch.diff",
  test_patch: "see patches/test_patch.diff",
};
const goldPatch = await fs.readFile(`${caseDir}/patches/gold_patch.diff`, "utf8");
const testPatch = await fs.readFile(`${caseDir}/patches/test_patch.diff`, "utf8");
const instance = {
  repo: spec.repo, instance_id: spec.instanceId, base_commit: spec.baseCommit,
  patch: goldPatch, test_patch: testPatch, problem_statement: spec.problemStatement,
  hints_text: "", created_at: spec.createdAt, version: spec.version,
  issue_id: spec.issueId, issue_url: spec.issueUrl,
  FAIL_TO_PASS: spec.failToPass, PASS_TO_PASS: spec.passToPass,
};
const writeJson = async (rel, data) => fs.writeFile(path.join(caseDir, rel), JSON.stringify(data, null, 2) + "\n");
if (!workbookOnly) {
if (spec.provenance) await writeJson("analysis/upstream_provenance.json", spec.provenance);
await writeJson(`analysis/source_row_${spec.caseNumber}.json`, source);
await fs.writeFile(`${caseDir}/analysis/source_material/single_pyc_case_${spec.caseNumber}.jsonl`, JSON.stringify(source) + "\n");
await writeJson(`analysis/source_material/single_pyc_swebench_standard_case_${spec.caseNumber}.json`, instance);
await writeJson(`official_swebench/instance_${spec.caseNumber}.json`, instance);
await fs.writeFile(`${caseDir}/official_swebench/instance_${spec.caseNumber}.jsonl`, JSON.stringify(instance) + "\n");
await writeJson(`official_swebench/public_task_${spec.caseNumber}.json`, {
  instance_id: spec.instanceId, repo: spec.repo, base_commit: spec.baseCommit,
  problem_statement: spec.problemStatement, hints_text: "", created_at: spec.createdAt,
  version: spec.version, issue_id: spec.issueId, issue_url: spec.issueUrl,
});
await writeJson("analysis/environment_spec.json", {
  instance_id: spec.sourceInstanceId, task_level: "integration", validation_type: spec.validationType ?? "official_pytest",
  environment: spec.environment ?? "requires_scipy_native_build", python_version_target: spec.pythonVersionTarget ?? "3.8",
  native_requirement: spec.nativeRequirement ?? "GCC, GFortran, OpenBLAS development libraries",
  build_system: spec.buildSystem ?? "SciPy setup.py build_ext -i at the verified base commit",
  test_execution: [spec.testExecution ?? "python3.8 -m pytest -vv <selected official nodes>"],
  runtime_verified: true,
  notes: [
    `The protected test patch is the exact upstream change in ${testFiles.join(", ")}.`,
    spec.verifiedError,
    `${spec.passToPass.length} unmodified neighboring tests pass on both Base and Gold.`,
  ],
  reproduction_status: "verified_base_fail_gold_pass_docker", base_commit: spec.baseCommit,
  fix_commit: spec.fixCommit, test_source: "official_project_tests", test_files: testFiles,
  FAIL_TO_PASS: spec.failToPass, PASS_TO_PASS: spec.passToPass,
});
await writeJson("official_swebench/metadata.json", {
  dataset_schema_version: "1.0", source_case: spec.sourceCase,
  candidate_case: spec.caseNumber,
  duplicate_source_cases_removed: spec.duplicateSourceCases ?? [],
  ...(spec.testScope ? { official_test_scope: spec.testScope } : {}),
  dataset_variant: "SWE-bench-compatible custom record", test_source: "official_project_tests",
  validation_type: spec.validationType ?? "official_pytest", created_at: spec.createdAt, created_at_precision: "date",
  instance_id: spec.instanceId, source_instance_id: spec.sourceInstanceId, repo: spec.repo,
  issue_id: spec.issueId, issue_url: spec.issueUrl, project_version: spec.version,
  base_commit: spec.baseCommit, fix_commit: spec.fixCommit,
  FAIL_TO_PASS: spec.failToPass, PASS_TO_PASS: spec.passToPass,
  verification: {
    container_engine: "Docker Desktop Linux containers", architecture: "linux/amd64",
    base_image: spec.baseImage ?? "public.ecr.aws/ubuntu/ubuntu:20.04", python_version: spec.pythonVersionLabel ?? "3.8.10", test_runner_version: spec.testRunnerVersion ?? "pytest 3.10.1",
    compiler_toolchain: spec.compilerToolchain ?? "GCC/GFortran and OpenBLAS from Ubuntu 20.04",
    base_target_status: spec.baseTargetStatus ?? "FAILED", base_regression_status: `${spec.passToPass.length} passed`,
    gold_target_status: `${spec.failToPass.length} passed`, gold_regression_status: `${spec.passToPass.length} passed`,
    result: "verified_base_fail_gold_pass_docker",
  },
});
await writeJson("evaluator/case_config.json", {
  template_version: "1.0", case_number: spec.caseNumber, instance_id: spec.instanceId,
  instance_file: `official_swebench/instance_${spec.caseNumber}.json`, repo_url: spec.repoUrl,
  base_commit: spec.baseCommit, fix_commit: spec.fixCommit, image: spec.image,
  python_version: spec.pythonVersionConfig ?? "3.8", numpy_version: spec.numpyVersion ?? "1.17.5", extra_apt_packages: [],
  runtime_assets: [{ source: "evaluator/case_adapter.sh", target: "/benchmark/case_adapter.sh" },
    ...(spec.additionalRuntimeAssets ?? []).map(({source, target}) => ({source, target}))],
  ...(spec.dockerRunArgs ? { docker_run_args: spec.dockerRunArgs } : {}),
});

const q = value => `'${value.replaceAll("'", "'\\''")}'`;
const testArgs = [...spec.passToPass, ...spec.failToPass].map(x => `        ${q(x)}`).join(" \\\n");
await fs.writeFile(`${caseDir}/evaluator/case_adapter.sh`, `#!/usr/bin/env bash\n\nbuild_project() {\n    ${spec.buildCommand ?? `${interpreter} setup.py build_ext -i`}\n}\n\nrun_project_tests() {\n    ${spec.testCommand ?? `${interpreter} -m pytest -c /dev/null -vv`} \\\n${testArgs}\n}\n`);

let dockerfile = await fs.readFile(spec.dockerfileSource, "utf8");
await fs.writeFile(`${caseDir}/evaluator/image/Dockerfile`, dockerfile);

const negative = `diff --git a/README.rst b/README.rst\n--- a/README.rst\n+++ b/README.rst\n@@ -1,3 +1,5 @@\n SciPy library main repository\n =============================\n \n+This evaluator control does not correct the target native-code defect.\n+\n`;
await fs.writeFile(`${caseDir}/verification/controls/negative_patch.diff`, spec.negativePatch ?? negative);
await fs.writeFile(`${caseDir}/verification/controls/tamper_patch.diff`, spec.tamperPatch);

await fs.writeFile(`${caseDir}/README.md`, `# Python-C to SWE-bench Case ${spec.caseNumber}\n\n## Identity\n\n- Instance ID: \`${spec.instanceId}\`\n- Source case: \`${spec.sourceCase}\`\n- Repository: \`${spec.repo}\`\n- Base: \`${spec.baseCommit}\`\n- Fix: \`${spec.fixCommit}\`\n- Upstream PR: <${spec.issueUrl}>\n\n## Verified relation\n\n${spec.targetSummary}. ${spec.passToPass.length} regressions pass on Base and Gold.\n\n## Directory contract\n\n- \`analysis/\`: source-row mapping, trace evidence, environment, and source material.\n- \`patches/\`: upstream product patch and exact official test patch.\n- \`official_swebench/\`: private/public task records, metadata, and checksums.\n- \`evaluator/\`: config-driven evaluator, SciPy adapter, and clean Dockerfile.\n- \`verification/\`: immutable image-build and patch-run evidence.\n\nThe verified evaluator image is \`${spec.image}\`.\n`);
await fs.writeFile(`${caseDir}/analysis/README.md`, `# Analysis\n\nThis directory preserves source Case ${spec.sourceCase}, the verified first-parent/fix mapping, upstream trace, environment requirements, and the generated workbook.\n\n${spec.verifiedError}\n`);
await fs.writeFile(`${caseDir}/official_swebench/README.md`, `# SWE-bench-compatible records\n\n- \`instance_${spec.caseNumber}.json\` contains the private record with product and official test patches.\n- \`instance_${spec.caseNumber}.jsonl\` is the single-line dataset form.\n- \`public_task_${spec.caseNumber}.json\` excludes the solution and protected test patch.\n- \`metadata.json\` records provenance and verified execution semantics.\n- \`SHA256SUMS.txt\` is generated after all artifacts are finalized.\n`);
await fs.writeFile(`${caseDir}/evaluator/README.md`, `# Evaluator\n\nThe evaluator applies the candidate patch first, then the protected official test patch, rebuilds SciPy's native extensions, and runs ${spec.failToPass.length} FAIL_TO_PASS plus ${spec.passToPass.length} PASS_TO_PASS nodes.\n`);
await fs.writeFile(`${caseDir}/verification/README.md`, `# Verification evidence\n\nRequired controls: Gold resolves FAIL_TO_PASS and preserves PASS_TO_PASS; negative remains unresolved; tamper is rejected before grading.\n`);
for (const rel of ["README.md", "analysis/README.md", "evaluator/README.md"]) {
  const docPath = path.join(caseDir, rel);
  const doc = await fs.readFile(docPath, "utf8");
  await fs.writeFile(docPath, doc.replaceAll("SciPy", project)
    .replace("Upstream PR:", "Upstream issue / PR:")
    .replace("verified first-parent/fix mapping", `verified ${spec.baseCommitStatus ?? "first-parent"}/fix mapping`));
}
}

if (process.argv.includes('--records-only')) {
  console.log(caseDir);
  process.exit(0);
}
const wb = Workbook.create();
const s1 = wb.worksheets.add("Source Record");
const s2 = wb.worksheets.add("SWE-bench Record");
const sourceRows = [
  [`Python-C Case ${spec.caseNumber} — Source and Trace Evidence`, ""], ["Field", "Value"],
  ["Source case", spec.sourceCase], ["Repository", spec.repo], ["Fix commit", spec.fixCommit],
  ["Base commit", spec.baseCommit], ["Upstream issue / PR", spec.issueUrl], ["Symptom", source.symptom],
  ["Bug location", source.bug_location], ["Bug location type", source.bug_location_type],
  ["Root cause", source.root_cause], ["Fixing strategy", source.fixing_strategy],
  ["Fix location", source.fix_location], ["Problem statement", spec.problemStatement],
  ...(spec.sourceTraceNotes ? [["Original source trace", source.bug_path], ["Source trace scope", spec.sourceTraceNotes]] : []),
  ["Verified Base trace", spec.verifiedError], ["Verified official test", spec.verifiedTest.replaceAll(" and ", "\n")],
  ...(spec.testScope ? [["Official test scope", spec.testScope]] : []),
  ...(spec.mergeIdentityLimitation ? [["PR merge identity limitation", spec.mergeIdentityLimitation]] : []),
];
const benchRows = [
  [`Python-C Case ${spec.caseNumber} — SWE-bench-compatible Record`, ""], ["Field", "Value"],
  ["Instance ID", spec.instanceId], ["Repository", spec.repo], ["Version", spec.version],
  ["Created at", spec.createdAt], ["Base commit", spec.baseCommit], ["Fix commit", spec.fixCommit],
  ...((spec.caseNumber === '048' || spec.workbookDateFields) && spec.mergedAt ? [["Merged at", spec.mergedAt]] : []),
  ["Issue / PR", spec.issueUrl], ["Test source", spec.testSourceLabel ?? "Official upstream pytest tests"],
  ...spec.failToPass.map((x, i) => [`FAIL_TO_PASS (${i + 1})`, x]),
  ...spec.passToPass.map((x, i) => [`PASS_TO_PASS (${i + 1})`, x]),
  ["Base / Gold outcome", spec.targetSummary], ["Docker image", spec.image],
  ["Problem statement", spec.problemStatement],
];
for (const [sheet, data] of [[s1, sourceRows], [s2, benchRows]]) {
  sheet.showGridLines = false; sheet.getRange(`A1:B${data.length}`).values = data;
  sheet.getRange(`A1:B${data.length}`).format.font = { name: "Aptos", size: 11, color: "#1F2937" };
  sheet.getRange("A1:B1").merge(); sheet.getRange("A1:B1").format = { fill: "#1F4E78", font: { name: "Aptos Display", size: 15, bold: true, color: "#FFFFFF" } };
  sheet.getRange("A2:B2").format = { fill: "#D9EAF7", font: { name: "Aptos", size: 11, bold: true, color: "#17365D" }, borders: { preset: "all", style: "thin", color: "#9FBAD0" } };
  sheet.getRange(`A3:A${data.length}`).format = { fill: "#EEF5FA", font: { name: "Aptos", size: 10, bold: true, color: "#17365D" }, borders: { preset: "all", style: "thin", color: "#D5E2EA" }, verticalAlignment: "top" };
  sheet.getRange(`B3:B${data.length}`).format = { font: { name: "Aptos", size: 10, color: "#1F2937" }, borders: { preset: "all", style: "thin", color: "#D5E2EA" }, wrapText: true, verticalAlignment: "top" };
  sheet.getRange("A:A").format.columnWidth = 25; sheet.getRange("B:B").format.columnWidth = 95;
  sheet.getRange(`A3:B${data.length}`).format.autofitRows(); sheet.freezePanes.freezeRows(2);
  if (spec.caseNumber === '048' || spec.workbookDateFields) {
    for (let i = 2; i < data.length; i++) {
      const text = String(data[i][1] ?? '');
      const lines = text.split('\n').reduce((sum, line) => sum + Math.max(1, Math.ceil(line.length / 103)), 0);
      sheet.getRange(`A${i+1}:B${i+1}`).format.rowHeight = Math.max(20, lines * 13 + 10);
    }
    if (sheet.name === 'SWE-bench Record') for (let i=0; i<data.length; i++) {
      if (['Created at','Merged at'].includes(data[i][0])) {
        const cell=sheet.getRange(`B${i+1}`);
        cell.values = [[(Date.parse(data[i][1] + 'T00:00:00Z') - Date.UTC(1899,11,30))/86400000]];
        cell.setNumberFormat('yyyy-mm-dd');
      }
    }
  }
}
wb.recalculate();
const inspect = await wb.inspect({ kind: "workbook,sheet", maxChars: 6000, tableMaxRows: 8, tableMaxCols: 3 });
await fs.writeFile(`${caseDir}/analysis/source_material/single_pyc_case_${spec.caseNumber}.xlsx.inspect.ndjson`, JSON.stringify(inspect) + "\n");
const formulaScan = [];
for (const sheetName of ["Source Record", "SWE-bench Record"]) formulaScan.push(await wb.inspect({ kind: "formula", sheetId: sheetName, range: "A1:B40", maxChars: 2000, options: { maxResults: 50 } }));
const errorScan = await wb.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",
  options: { useRegex: true, maxResults: 300 },
  summary: "final formula error scan",
});
if (spec.workbookDateFields) {
  const checks = [];
  for (const [sheet, data] of [[s1, sourceRows], [s2, benchRows]]) {
    const result = await wb.inspect({ kind: "table", sheetId: sheet.name, range: `A1:B${data.length}`, include: "values,formulas", tableMaxRows: data.length, tableMaxCols: 2, maxChars: 14000 });
    checks.push({ sheet: sheet.name, ndjson: result.ndjson ?? null, inspection: result });
  }
  await fs.writeFile(`${caseDir}/analysis/source_material/workbook_value_checks.json`, JSON.stringify({checks,errorScanNdjson:errorScan.ndjson ?? null},null,2)+'\n');
}
await fs.writeFile(`${root}/_work/pyc_batch/case${spec.caseNumber}_formula_scan.json`, JSON.stringify({ formulaScan, errorScan }, null, 2));
for (const sheetName of ["Source Record", "SWE-bench Record"]) {
  const preview = await wb.render({ sheetName, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(`${root}/_work/pyc_batch/case${spec.caseNumber}_${sheetName.toLowerCase().replaceAll(" ", "_")}.png`, new Uint8Array(await preview.arrayBuffer()));
}
const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(`${caseDir}/analysis/source_material/single_pyc_case_${spec.caseNumber}.xlsx`);
console.log(caseDir);
