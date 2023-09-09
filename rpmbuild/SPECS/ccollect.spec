Summary:        (pseudo) incremental backup with different exclude lists using hardlinks and rsync
Name:           ccollect
Version:        2.10
Release:        5%{?dist}
URL:            https://www.nico.schottelius.org/software/ccollect
Source0:        https://www.nico.schottelius.org/software/ccollect/download/%{name}-%{version}.tar.bz2
Patch1:         ccollect-2.9-rsync3.patch
Patch2:         https://code.ungleich.ch/ungleich-public/ccollect/commit/2ca7598593befc52bff6b51b330bbcf508e20387.patch

License:        GPL-3
Group:          Applications/System
Vendor:         Nico Schottelius <nico-ccollect@schottelius.org>
BuildRoot:      %{_tmppath}/%{name}-%(id -un)
BuildArch:	noarch
Requires:	rsync

%description
Ccollect backups data from local and remote hosts to your local harddisk.
Although ccollect creates full backups, it requires very less space on the backup medium, because ccollect uses hardlinks to create an initial copy of the last backup.
Only the inodes used by the hardlinks and the changed files need additional space.

%prep
%setup -q

%patch1 -p1
%patch2 -p1

%install
rm -rf $RPM_BUILD_ROOT

#Installing main ccollect and /etc directory
%__install -d 755 %buildroot%_bindir
%__install -m 755 ccollect %buildroot%_bindir/

%__install -d 750 %buildroot%_sysconfdir/%name
%__install -d 750 %buildroot%_sysconfdir/%name/defaults
%__install -d 750 %buildroot%_sysconfdir/%name/defaults/intervals
%__install -d 750 %buildroot%_sysconfdir/%name/sources

#bin files from tools directory
for t in $(ls tools/ccollect_*) ; do
	%__install -m 755 ${t} %buildroot%_bindir/
done

#Configuration examples and docs
%__install -d 755 %buildroot%_datadir/doc/%name-%version/examples

%__install -m 644 README %buildroot%_datadir/doc/%name-%version
%__install -m 644 COPYING %buildroot%_datadir/doc/%name-%version
%__install -m 644 CREDITS %buildroot%_datadir/doc/%name-%version
%__install -m 644 conf/README %buildroot%_datadir/doc/%name-%version/examples
%__cp -pr conf/defaults %buildroot%_datadir/doc/%name-%version/examples/
%__cp -pr conf/sources %buildroot%_datadir/doc/%name-%version/examples/

#Addition documentation and some config tools
%__install -d 755 %buildroot%_datadir/%name/tools
%__install -m 755 tools/called_from_remote_pre_exec %buildroot%_datadir/%name/tools
%__cp -pr tools/config-pre-* %buildroot%_datadir/%name/tools
%__install -m 755 tools/report_success %buildroot%_datadir/%name/tools

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%_bindir/ccollect*
%_datadir/doc/%name-%version
%_datadir/%name/tools
%docdir %_datadir/doc/%name-%version
%defattr(644, root, root, 750)
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/defaults
%dir %_sysconfdir/%name/defaults/intervals
%dir %_sysconfdir/%name/sources

%changelog
* Sun Sep 10 2023 Jun Futagawa <jfut@integ.jp> 2.10-5
- Add initial intervals directory (#4)

* Sat Sep  9 2023 Jun Futagawa <jfut@integ.jp> 2.10-4
- Add initial configuration directory (#3)

* Sun May 29 2022 Jun Futagawa <jfut@integ.jp> 2.10-3
- Add support for RHEL/AlmaLinux/Rocky Linux 9 (#1)

* Sat Nov 28 2020 Jun Futagawa <jfut@integ.jp> 2.10-2
- Add improve 'current' symlink to backup destinations patch

* Wed Nov 25 2020 Jun Futagawa <jfut@integ.jp> 2.10-1
- Update to version 2.10

* Sun Aug 16 2020 Jun Futagawa <jfut@integ.jp> 2.9-1
- Update to version 2.9
- Change the rsync option for rsync 3.x when checking the connection to the source

* Thu Nov 14 2019 Jun Futagawa <jfut@integ.jp> 2.6-1
- Update to version 2.6

* Thu Aug 20 2009 Nico Schottelius <nico-ccollect@schottelius.org> 0.8
- Introduce consistenst time sorting (John Lawless)
- Check for source connectivity before trying backup (John Lawless)
- Defensive programming patch (John Lawless)
- Some code cleanups (argument parsing, usage) (Nico Schottelius)
- Only consider directories as sources when using -a (Nico Schottelius)
- Fix general parsing problem with -a (Nico Schottelius)
- Fix potential bug when using remote_host, delete_incomplete and ssh (Nico Schottelius)
- Improve removal performance: minimised number of 'rm' calls (Nico Schottelius)
- Support sorting by mtime (John Lawless)
- Improve option handling (John Lawless)
- Add support for quiet operation for dead devices (quiet_if_down) (John Lawless)
- Add smart option parsing, including support for default values (John Lawless)
- Updated and cleaned up documentation (Nico Schottelius)
- Fixed bug "removal of current directory" in ccollect_delete_source.sh (Found by G????nter St????hr, fixed by Nico Schottelius)

