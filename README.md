# ccollect RPM Packaging

[![Build Status](https://github.com/jfut/ccollect-rpm/workflows/test/badge.svg?branch=master)](https://github.com/jfut/ccollect-rpm/actions?query=workflow%3Atest)

[ccollect](https://www.nico.schottelius.org/software/ccollect/) RPM Packaging for RHEL/AlmaLinux/Rocky Linux/others.

## Usage

```
Usage:
    build [-d] [-h] BUILD_IMAGE_NAME

    Options:
        -d Debug mode.

    Build for RHEL/AlmaLinux/Rocky Linux 9:
        build almalinux:9

    Build for RHEL/AlmaLinux/Rocky Linux 8:
        build almalinux:8

    Build for CentOS 7:
        build centos:7
```

## Build RPM Packages with Docker

You can build RPM packages in Docker.

```
./build almalinux:9
```

- Debug shell

```
./build -d almalinux:9
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

