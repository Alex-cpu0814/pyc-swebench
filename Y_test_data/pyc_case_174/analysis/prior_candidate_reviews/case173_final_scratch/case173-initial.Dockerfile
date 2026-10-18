FROM public.ecr.aws/docker/library/python:3.8.20-bullseye@sha256:11da1db2f485e2560be9817f92932a29f68fefc332b0167e8c51ae308ee23337
ARG DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update && apt-get install -y --no-install-recommends cmake && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED=1 LC_ALL=C.UTF-8 LANG=C.UTF-8
RUN git init /opt/googletest && cd /opt/googletest && git remote add origin https://github.com/google/googletest.git && git fetch --depth=1 --no-tags origin 58d77fa8070e8cec2dc1ed015d66b454c8d78850 && git checkout --detach FETCH_HEAD && git remote remove origin && test "$(git rev-parse HEAD)" = 58d77fa8070e8cec2dc1ed015d66b454c8d78850
ARG REPO_URL=https://github.com/spglib/spglib.git
ARG BASE_COMMIT=9218fa14771d967a20f00764b335bc2a265790a1
ARG INSTANCE_ID=spglib__spglib-36d570bc
RUN git init /testbed && cd /testbed && git remote add origin "${REPO_URL}" && git fetch --depth=1 --no-tags origin "${BASE_COMMIT}" && git checkout --detach "${BASE_COMMIT}" && git remote remove origin && git config core.autocrlf false && test "$(git rev-parse HEAD)" = "${BASE_COMMIT}"
WORKDIR /testbed
RUN cmake -S test -B build -DFETCHCONTENT_SOURCE_DIR_GOOGLETEST=/opt/googletest && cmake --build build --target test_magnetic_symmetry --parallel 2 && test -x /testbed/build/test_magnetic_symmetry && test "$(git -C /opt/googletest rev-parse HEAD)" = 58d77fa8070e8cec2dc1ed015d66b454c8d78850 && /testbed/build/test_magnetic_symmetry --gtest_list_tests && printf '%s\n' '/build/' >> .git/info/exclude && test -z "$(git status --porcelain)"
CMD ["/bin/bash"]
