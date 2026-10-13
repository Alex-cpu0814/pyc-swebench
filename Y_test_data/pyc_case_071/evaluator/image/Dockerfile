FROM public.ecr.aws/docker/library/python:3.8.20-bullseye@sha256:11da1db2f485e2560be9817f92932a29f68fefc332b0167e8c51ae308ee23337
ARG DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV PYTHONUNBUFFERED=1 LC_ALL=C.UTF-8 LANG=C.UTF-8 PYTHONPATH=/testbed
RUN sed -i '/bullseye-security/d; s|http://deb.debian.org|https://deb.debian.org|g' /etc/apt/sources.list \
    && apt-get -o Acquire::Retries=5 update \
    && apt-get -o Acquire::Retries=5 install -y --no-install-recommends --no-upgrade gcc=4:10.2.1-1 g++=4:10.2.1-1 git ca-certificates \
    && rm -rf /var/lib/apt/lists/*
RUN python -m pip install --no-cache-dir pip==24.3.1 setuptools==68.2.2 wheel==0.42.0 setuptools_scm==6.4.2 \
       pytest==7.4.4 packaging==23.2 pluggy==1.3.0 iniconfig==2.0.0 exceptiongroup==1.2.2 tomli==2.0.1
ARG REPO_URL=https://github.com/ultrajson/ultrajson.git
ARG BASE_COMMIT=f26f9679f1b9d7fa2d0488e1e7b1256d9391a85f
ARG INSTANCE_ID=ultrajson__ultrajson-441
RUN git init /testbed && cd /testbed \
    && git remote add origin "${REPO_URL}" \
    && git fetch --no-tags origin "${BASE_COMMIT}" refs/tags/4.0.1:refs/tags/4.0.1 \
    && git checkout --detach "${BASE_COMMIT}" \
    && git remote remove origin \
    && git config core.autocrlf false \
    && test "$(git rev-parse HEAD)" = "${BASE_COMMIT}" \
    && test "$(git rev-parse 4.0.1)" = "0b5b6358893a4b593c2f977f67f1f7cce0dce0ec" \
    && test "$(git rev-list --count 4.0.1..HEAD)" = "3"
WORKDIR /testbed
RUN python setup.py build_ext -i --force \
    && python -c 'import ujson; print(ujson.__version__,ujson.__file__); assert ujson.__version__ == "4.0.2.dev3"; assert ujson.__file__.startswith("/testbed/ujson.")' \
    && git restore --source=HEAD --worktree -- . \
    && test -z "$(git status --porcelain)"
CMD ["/bin/bash"]
