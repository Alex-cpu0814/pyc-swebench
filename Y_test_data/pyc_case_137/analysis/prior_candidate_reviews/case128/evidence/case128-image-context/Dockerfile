FROM public.ecr.aws/docker/library/python:3.8.20-bullseye@sha256:11da1db2f485e2560be9817f92932a29f68fefc332b0167e8c51ae308ee23337
ARG DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV PYTHONUNBUFFERED=1 LC_ALL=C.UTF-8 LANG=C.UTF-8 PYTHONPATH=/testbed
RUN sed -i '/bullseye-security/d; s|http://deb.debian.org|https://deb.debian.org|g' /etc/apt/sources.list && apt-get -o Acquire::Retries=5 update && apt-get -o Acquire::Retries=5 install -y --no-install-recommends gcc=4:10.2.1-1 git ca-certificates && rm -rf /var/lib/apt/lists/*
RUN python -m pip install --no-cache-dir pip==24.3.1 setuptools==68.2.2 wheel==0.42.0 pytest==7.4.4 packaging==23.2 pluggy==1.3.0 iniconfig==2.0.0 exceptiongroup==1.2.2 tomli==2.0.1
ARG REPO_URL=https://github.com/MSeifert04/iteration_utilities.git
ARG BASE_COMMIT=5e2f2df0ba543352ae28d7b4c23d0be1008aebf6
ARG INSTANCE_ID=MSeifert04__iteration_utilities-200
RUN git init /testbed && cd /testbed && git remote add origin "${REPO_URL}" && git fetch --depth=1 --no-tags origin "${BASE_COMMIT}" && git checkout --detach "${BASE_COMMIT}" && git remote remove origin && git config core.autocrlf false && test "$(git rev-parse HEAD)" = "${BASE_COMMIT}"
WORKDIR /testbed
RUN python setup.py build_ext --inplace --force && python -c "import iteration_utilities,_iteration_utilities; print(iteration_utilities.__version__,_iteration_utilities.__file__); assert iteration_utilities.__version__ == '0.6.0'; assert _iteration_utilities.__file__.startswith('/testbed/_iteration_utilities.')" && git restore --source=HEAD --worktree -- . && printf '%s\n' '/build/' '**/__pycache__/' '*.pyc' '*.so' '/iteration_utilities.egg-info/' >> .git/info/exclude && test -z "$(git status --porcelain)"
CMD ["/bin/bash"]
