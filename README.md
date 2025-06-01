# ccollect RPM Packaging

[![Build Status](https://github.com/jfut/ccollect-rpm/workflows/test/badge.svg?branch=master)](https://github.com/jfut/ccollect-rpm/actions?query=workflow%3Atest)

[ccollect](https://www.nico.schottelius.org/software/ccollect/) RPM Packaging for RHEL/AlmaLinux/Rocky Linux/others.

## Usage

```
Usage:
    build [-d] [-h] BUILD_IMAGE_NAME

    Options:
        -d Debug mode.

    Build for RHEL/AlmaLinux/Rocky Linux 10:
        build almalinux:10

    Build for RHEL/AlmaLinux/Rocky Linux 9:
        build almalinux:9

    Build for RHEL/AlmaLinux/Rocky Linux 8:
        build almalinux:8
```

## Build RPM Packages with Docker

You can build RPM packages in Docker.

```
./build almalinux:10
```

- Debug shell

```
./build -d almalinux:10
/pkg/build-rpm /pkg/rpmbuild ccollect.spec
```

## Release

1. Edit the `Draft` on the release page.
2. Update the new version `name` and `tag` on the edit page.
3. Check `Set as a pre-release` and press the `Publish release` button.
4. Wait for the build by GitHub Actions to finish.
    - If the build fails due to errors such as download errors of source files, execute `Re-run failed jobs`.
5. Once all release files are automatically uploaded, check `Set as the latest release` and press the `Publish release` button.

## License

MIT
