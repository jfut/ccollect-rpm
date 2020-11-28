# ccollect RPM Packaging

[![Build Status](https://github.com/jfut/ccollect-rpm/workflows/test/badge.svg?branch=master)](https://github.com/jfut/ccollect-rpm/actions?query=workflow%3Atest)

RPM Packaging for [ccollect](https://www.nico.schottelius.org/software/ccollect/).

## Usage

```
Usage:
    build [-d] [-h] BUILD_IMAGE_NAME

    Options:
        -d Debug mode.

    Build for CentOS 8:
        build centos:8

    Build for CentOS 7:
        build centos:7
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
git tag -a v2.10-2 -m "Release v2.10-2"
git push origin refs/tags/v2.10-2
```

## License

MIT

