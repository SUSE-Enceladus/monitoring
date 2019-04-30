#
# spec file for package monitoring-plugins-proc-timed-hang
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           monitoring-plugins-proc-timed-hang
Version:        20170906
Release:        0
Summary:        Check a process against expiration time
License:        GPL-2.0
Group:          System/Monitoring
Url:            https://github.com/SUSE-Enceladus/monitoring
Source0:        check_proc_timed_hang_%{version}.tar.bz2
Provides:       nagios-plugins-proc-timed-hang = %{version}-%{release}
Obsoletes:      nagios-plugins-proc-timed-hang < %{version}-%{release}
BuildRequires:  nagios-rpm-macros
Requires:       python-docopt
Requires:       python-python-dateutil
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The script monitors a given process and if the process runs longer than the
specified time it is marked as critical or optionally killed. If the kill
operation fails the process is also marked as critical.

This is useful to monitor long running processes that may get stuck. One needs
to have an idea about the expected run time of the process. This is not useful
for monitoring time critical processes. The check can only be used on processes
that have a singular instance, i.e. there can only be one entry in the process
table for the process with the given name.

%prep
%setup -q -n check_proc_timed_hang_%{version}

%install
install -D -m755 check_proc_timed_hang %{buildroot}/%{nagios_plugindir}/check_proc_timed_hang

%files
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%doc LICENSE
%{nagios_plugindir}/check_proc_timed_hang


%changelog
