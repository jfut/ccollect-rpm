# ccollect RPM Packaging

[![Build Status](https://github.com/jfut/ccollect-rpm/workflows/test/badge.svg?branch=master)](https://github.com/jfut/ccollect-rpm/actions?query=workflow%3Atest)

## Usage

```
Usage:
    build [-d] [-h] BUILD_IMAGE_NAME

    Options:
        -d Debug mode.

    Build for CentOS 8:
        build -i centos:8

    Build for CentOS 7:
        build -i centos:7
```

## Build RPM Packages with Docker

You can build RPM packages in Docker.

```
./build
```

- Debug shell

```
./build -d
/pkg/build-rpm /pkg/rpmbuild ccollect.spec
```

## Release tag

e.g.:

```
git tag -a v2.6-1 -m "Release v2.6-1"
git push origin refs/tags/v2.6-1
```

