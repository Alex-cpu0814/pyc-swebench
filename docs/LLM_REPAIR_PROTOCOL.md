# LLM 修复实验指南

版本：**1.0**　更新：**2026-10-19**

本指南规定如何使用本数据集进行“人工提供源码上下文、纯 LLM 生成补丁、Docker 独立评测”的实验。所有模型使用相同的案例集合、输入准备规则与轮次预算。已有试运行保留实际设置，不追溯标记为遵循本版本。

**流程：公开任务 → 固定 Base 源码 → 模型输入 → 候选补丁 → Docker 评测 → 结果记录。**

## 1. 实验设置

| 项目 | 默认规则 |
| --- | --- |
| 模型输入 | 公开问题描述、固定 Base 的相关生产源码、统一提示词 |
| 文件定位 | 人工依据公开问题和 Base 源码搜索，记录关键词与提供的文件范围 |
| 模型权限 | 不联网、不调用文件或命令工具；每个案例、每个模型开启独立对话 |
| 源码范围 | 默认提供选中文件的完整内容，按修复前调用关系补充定义和声明 |
| 上下文预算 | 实验开始前登记统一上限及计量方式；超限时不得静默截断 |
| 候选预算 | 每个案例、每个模型最多 **2 轮**：首轮候选，以及一次失败日志反馈后的修订 |
| 模型信息 | 记录名称、版本、使用平台、生成时间与可见采样参数；不可见的信息填写“未知” |
| 结果判定 | 以本案例评测器生成的 `summary.json` 及原始日志为依据 |

使用源码选段、其他候选预算、独立重采样或 agent 时，另行登记设置并分组报告。`NEED_CONTEXT` 等补充请求单独计数，保存每条追加输入；包含补充请求的首轮需明确标注，不能算作一次无补充的模型调用。

## 2. 哪些材料提供给模型

| 材料 | 用途 |
| --- | --- |
| `official_swebench/public_task_NNN.json` | 提供公开任务；保留原文件用于追溯 |
| `repo` 对应项目在 `base_commit` 的源码 | 提供修复前代码；保留仓库相对路径 |
| 统一提示词 | 规定候选补丁的输出形式 |
| 参考修复、`instance_NNN.json/jsonl`、`patches/`、`analysis/`、`verification/` | 不提供给模型，也不用于人工定位待修改文件 |
| 评测器、测试补丁及评分配置 | 仅由评测端使用，不作为首轮输入 |

从问题中的符号、API 或报错出发搜索，再沿 Base 调用关系选择上下文。不要通过参考补丁、上游修复 PR 或后续提交决定提供哪些文件。已存在于 Base 的普通测试与本案例追加的评测测试应区分；本协议默认首轮只提供生产源码。

仓库不要求预先存在 `LLM_INPUT.txt`。使用者可以上传公开任务和源码文件，也可以自行合并为文本包。两种方式均需保存实际输入、文件列表、行号范围（若为选段）及 SHA256。不同模型尽量使用相同输入；若必须缩减上下文，另行登记设置。

## 3. 从下载数据到运行评测

以下以 **007** 为例，在 **Windows PowerShell** 中操作。先进入克隆得到的本仓库根目录。需要安装 Python、Docker，并启动 Docker Desktop。

### ① 读取任务，拉取镜像

```powershell
$repoRoot = (Get-Location).Path
$caseDir = Join-Path $repoRoot 'Y_test_data/pyc_case_007'
$task = Get-Content -Raw -Encoding UTF8 (Join-Path $caseDir 'official_swebench/public_task_007.json') | ConvertFrom-Json
$image = (Get-Content -Raw -Encoding UTF8 (Join-Path $caseDir 'evaluator/case_config.json') | ConvertFrom-Json).image
$task | Select-Object instance_id, repo, base_commit, problem_statement
docker pull $image
```

配置文件仅用于读取镜像等评测设置，不发送给模型。实验记录保存数据集 Git 提交、`base_commit` 和实际镜像 ID 或 digest。

### ② 导出修复前源码

以下命令将实验资料放在本仓库的同级目录，源码导出位置应为空目录。

```powershell
$trialDir = Join-Path (Split-Path -Parent $repoRoot) 'repair_trials/case007/llm_attempt01'
$sourceDir = Join-Path $trialDir 'source_base'
New-Item -ItemType Directory -Force -Path $sourceDir | Out-Null
docker run --rm --mount "type=bind,source=$sourceDir,target=/export" --entrypoint bash $image -lc "set -euo pipefail; git -C /testbed archive $($task.base_commit) | tar -x -C /export"
```

这会从镜像中的 `/testbed` 导出指定 Base 的已跟踪源码，不导出 Git 历史，也不应用候选或评测测试补丁。

例如，公开问题提到 `_ArrayMemoryError`，可据此搜索：

```powershell
Get-ChildItem -Path (Join-Path $sourceDir 'numpy/core') -Recurse -File -Include *.c,*.h,*.py | Select-String -SimpleMatch '_ArrayMemoryError' | Select-Object Path,LineNumber,Line
```

根据搜索结果选择生产源码，保存搜索关键词、选择理由和文件范围。其他案例使用各自公开问题中的关键词，不沿用 007 的符号或路径。

### ③ 向 LLM 提交输入

上传公开任务及选定源码，同时发送以下提示词。将占位内容替换为本案例信息，并保留实际发送版本。

```text
请根据公开任务中的问题描述，修复提供的源码。
Base commit：<公开任务中的 base_commit>
文件路径：<逐个列出源码文件在原仓库中的相对路径>

请自行分析问题，只修改必要的生产代码，保持无关行为兼容。
不要联网查询上游修复、参考补丁或后续提交。
最终只输出相对于原始 Base 的完整 unified diff。
路径使用 a/<仓库相对路径> 和 b/<仓库相对路径>。
不要输出 Markdown 围栏、解释或省略号。
如果必要上下文不足，请以 NEED_CONTEXT 开头，列出需要的修复前文件或符号。
未经实际执行，不要声称测试通过。
```

模型请求补充上下文时，只按前述定位规则提供修复前源码，保存追加消息。记录模型实际读取的输入；输入被产品截断或文件未成功读取时，不应直接视作有效的既定上下文实验。

### ④ 保存候选补丁

原始模型回复保存为 `response_raw.txt`，纯补丁以 UTF-8 保存为 `model_patch.diff`。允许去除 Markdown 围栏、统一换行、纠正 hunk 行号和长度、补齐 Base 中未修改的上下文；必须保留模型原有的代码增删及其应用位置。

保留格式处理记录、处理前后哈希和原始补丁可应用性。若无法在不改变模型代码改动含义的情况下规范化，记录为无可应用候选，不由人工或辅助模型补写修复逻辑。报告中说明成功率是否允许格式规范化。

### ⑤ 手动运行评测

继续在同一 PowerShell 会话中执行：

```powershell
python (Join-Path $caseDir 'evaluator/evaluate_model_patch.py') --docker docker --image $image --patch (Join-Path $trialDir 'model_patch.diff') --output-root (Join-Path $trialDir 'evaluation') --run-id case-007-llm-attempt-01 --label llm-first-candidate --timeout 1800
```

无需执行 `.ps1` 包装脚本。评测器会在容器中应用候选和评测测试补丁，完成项目构建、测试及评分。部分案例使用 debug Python、泄漏检测或其他专用设置，不以自行运行普通 pytest 代替正式评测。

结果位于 `evaluation/case-007-llm-attempt-01/`：

| 文件 | 用途 |
| --- | --- |
| `summary.json` | 最终状态、补丁哈希、镜像信息和测试统计 |
| `grading.json` | 各项指定测试的评分结果 |
| `tests.raw.log` | 原始测试输出及失败详情 |
| `project-build.raw.log`、`events.jsonl` 等 | 构建与执行过程记录 |

`resolved` 表示通过本案例评测，`unresolved` 表示未通过，`error` 需要结合原因及日志排查。补丁应用错误、生成失败和环境故障应分别记录；不能将环境故障判为修复成功。

### ⑥ 可选：收到反馈后的第二轮

首轮未成功时，在同一模型对话中提供首轮状态及 `tests.raw.log` 中全部失败项的原始报错。若失败由编译或补丁应用导致，提供对应原始诊断。仅附必要的诊断，不提供参考修复或额外的测试补丁全文，也不附人工修复建议。

第二轮仍输出**相对于原始 Base 的完整补丁**，包含需要保留的首轮改动。另存为 `llm_attempt02`，使用新的 `run_id`，保留首轮所有文件。模型首轮成功即停止；两轮后仍未成功也停止。环境故障可修复环境后对同一候选重新评测，使用新 `run_id` 并记录原因，不增加模型候选轮次。

## 4. 记录与统计

每个案例、模型和轮次至少保存以下信息：

| 类别 | 记录内容 |
| --- | --- |
| 版本 | 协议版本、数据集 Git 提交、案例 ID、Base 提交、镜像 ID/digest |
| 模型 | 名称及版本、平台、可见参数、生成时间 |
| 输入 | 实际提示词、源码文件/行号、选择依据、上下文预算及追加消息 |
| 输出 | 原始回复、候选补丁、格式处理说明、处理前后 SHA256 |
| 反馈 | 第二轮实际收到的日志或诊断；无反馈则注明 |
| 评测 | `run_id`、状态、目标/回归测试统计、完整结果目录 |

每个模型使用事先固定的案例集合及案例数 **N**。分别报告：

- **首次修复成功率**：首轮 `resolved` 的案例数 / N。
- **两轮内修复成功率**：最多两轮中至少一次 `resolved` 的案例数 / N，并注明第二轮允许评测反馈。
- **格式可应用率与异常数量**：单独报告原始补丁可应用性、生成失败、格式失败、上下文不足及环境故障。

同一案例多轮成功只计一次。测试通过项占比不等于案例修复成功率。不得事后剔除失败案例来缩小 N；未完成或环境故障需列出并说明覆盖情况。没有反馈的独立重试与收到日志后的修订分组统计，不混报为同一种成功率。

## 5. 目录约定

```text
repair_trials/caseNNN/
├── llm_attempt01/
│   ├── README.md             # 本轮模型、设置、输入范围及结果
│   ├── response_raw.txt      # 原始模型回复
│   ├── model_patch.diff      # 实际评测的候选
│   ├── source_base/          # 固定 Base 源码，可供后续轮次引用
│   ├── input_materials/      # 实际输入、来源、文件范围及哈希
│   ├── format_checks/        # 如有格式处理，保存记录
│   └── evaluation/           # 评测器输出
└── llm_attempt02/             # 如有反馈修订，独立保存
```

测试通过表示满足该案例的评测标准。仓库主 README 中的 Base/Gold 验证用于确认数据集及测试有效，不代表任何 LLM 已完成修复。
