FROM public.ecr.aws/ubuntu/ubuntu:18.04@sha256:975b418c2c6c72bdfb978ac631c3fae2f42b752f5ab29dec706a01f3f6acc14b
ARG DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update && apt-get install -y --no-install-recommends build-essential ca-certificates git pkg-config python-minimal python2.7 python2.7-dev lua5.1 liblua5.1-0-dev && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED=1 LC_ALL=C.UTF-8 LANG=C.UTF-8 PYTHONPATH=/testbed PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
RUN mkdir -p /usr/local/lib/pkgconfig && ln -s "$(pkg-config --variable=pcfiledir lua5.1)/lua5.1.pc" /usr/local/lib/pkgconfig/lua.pc && pkg-config --modversion lua && pkg-config --libs --cflags lua
ARG REPO_URL=https://github.com/bastibe/lunatic-python.git
ARG BASE_COMMIT=d9033bcf19b5f8404c7ee61f35e001fcfd603614
ARG INSTANCE_ID=bastibe__lunatic-python-bf894ed5
RUN git init /testbed && cd /testbed && git remote add origin "${REPO_URL}" && git fetch --depth=1 --no-tags origin "${BASE_COMMIT}" && git checkout --detach "${BASE_COMMIT}" && git remote remove origin && git config core.autocrlf false && test "$(git rev-parse HEAD)" = "${BASE_COMMIT}"
WORKDIR /testbed
RUN python2.7 setup.py build_ext --inplace --force && python2.7 -c "import lua,os; print(os.path.realpath(lua.__file__),lua.eval('_VERSION')); assert os.path.realpath(lua.__file__) == '/testbed/lua.so'; assert lua.eval('_VERSION') == 'Lua 5.1'" && git checkout HEAD -- . && printf '%s\n' '/build/' '*.pyc' '*.so' >> .git/info/exclude && test -z "$(git status --porcelain)"
CMD ["/bin/bash"]
