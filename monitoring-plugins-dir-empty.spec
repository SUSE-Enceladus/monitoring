#
# spec file for package monitoring-plugins-dir-empty
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


Name:           monitoring-plugins-dir-empty
Version:        20170912
Release:        0
Summary:        Check a directory is empty or does not exist
License:        GPL-2.0
Group:          System/Monitoring
Url:            https://github.com/SUSE-Enceladus/monitoring
Source0:        check_dir_empty_%{version}.tar.bz2
Provides:       nagios-plugins-check_dir_empty = %{version}-%{release}
Obsoletes:      nagios-plugins-check_dir_empty < %{version}-%{release}
Requires:       python3
Requires:       python3-docopt
BuildRequires:  nagios-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description

The script monitors that a given directory is/remains empty or does not exist

%prep
%setup -q -n check_dir_empty_%{version}

%install
install -D -m755 check_dir_empty %{buildroot}/%{nagios_plugindir}/check_dir_empty

%files
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%doc LICENSE
%{nagios_plugindir}/check_dir_empty

%changelog
