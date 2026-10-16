FROM --platform=linux/386 public.ecr.aws/ubuntu/ubuntu:18.04@sha256:fc896f56642f382e99601461c683dee1534f0d4cb7e17bcb3494d5ed0f3a8a06
ARG DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update && apt-get install -y --no-install-recommends build-essential ca-certificates git pkg-config python-minimal python2.7 python2.7-dev libsqlite3-dev && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED=1 LC_ALL=C.UTF-8 LANG=C.UTF-8 PYTHONPATH=/testbed/build/pysqlite_lib
ARG REPO_URL=https://github.com/ghaering/pysqlite.git
ARG BASE_COMMIT=b124ba3992dbd3d87a7cf5609e8acba952c2a3cf
ARG INSTANCE_ID=ghaering__pysqlite-ae4c5454
RUN git init /testbed && cd /testbed && git remote add origin "${REPO_URL}" && git fetch --depth=1 --no-tags origin "${BASE_COMMIT}" && git checkout --detach "${BASE_COMMIT}" && git remote remove origin && git config core.autocrlf false && test "$(git rev-parse HEAD)" = "${BASE_COMMIT}"
WORKDIR /testbed
RUN python2.7 setup.py build --build-lib /testbed/build/pysqlite_lib --force && python2.7 -c "import pysqlite2.dbapi2 as db,pysqlite2._sqlite as native,struct,sys; print(db.version,db.sqlite_version,native.__file__,struct.calcsize('P')*8,type(2**40).__name__); assert db.version == '2.0.alpha4'; assert struct.calcsize('P')*8 == 32; assert type(2**40) is long; assert native.__file__.startswith('/testbed/build/pysqlite_lib/pysqlite2/_sqlite')" && git checkout HEAD -- . && printf '%s\n' '/build/' '*.pyc' >> .git/info/exclude && test -z "$(git status --porcelain)"
CMD ["/bin/bash"]
