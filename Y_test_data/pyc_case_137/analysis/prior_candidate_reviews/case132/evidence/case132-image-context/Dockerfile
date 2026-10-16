FROM public.ecr.aws/docker/library/python:3.6.15-buster@sha256:56ba32a1c5aa030914cc957f1c9fe58d9d462bdf89a1e5f2b4dbdda68085327e
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV PYTHONUNBUFFERED=1 LC_ALL=C.UTF-8 LANG=C.UTF-8 PYTHONPATH=/testbed
RUN python -m pip install --no-cache-dir pip==21.3.1 setuptools==59.6.0 wheel==0.37.1 pytest==3.0.7 py==1.4.34
ARG REPO_URL=https://github.com/MSeifert04/iteration_utilities.git
ARG BASE_COMMIT=d12877a91ada393525ad5209edb88da491792646
ARG INSTANCE_ID=MSeifert04__iteration_utilities-198
RUN git init /testbed && cd /testbed && git remote add origin "${REPO_URL}" && git fetch --depth=1 --no-tags origin "${BASE_COMMIT}" && git checkout --detach "${BASE_COMMIT}" && git remote remove origin && git config core.autocrlf false && test "$(git rev-parse HEAD)" = "${BASE_COMMIT}"
WORKDIR /testbed
RUN python setup.py build_ext --inplace --force && python -c "import iteration_utilities,_iteration_utilities; print(iteration_utilities.__version__,_iteration_utilities.__file__); assert iteration_utilities.__version__ == '0.5.2'; assert _iteration_utilities.__file__.startswith('/testbed/_iteration_utilities.')" && git checkout HEAD -- . && printf '%s\n' '/build/' '**/__pycache__/' '*.pyc' '*.so' '/iteration_utilities.egg-info/' >> .git/info/exclude && test -z "$(git status --porcelain)"
CMD ["/bin/bash"]
