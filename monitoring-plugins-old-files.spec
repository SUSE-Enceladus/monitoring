#
# spec file for package monitoring-plugins-old-files.spec
#
# Copyright (c) 2019 SUSE LLC
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


Name:           monitoring-plugins-old-files
Version:        20190612
Release:        0
Summary:        Monitor presence of files older than given time
License:        GPL-2.0
Group:          System/Monitoring
Url:            https://github.com/SUSE-Enceladus/monitoring
Source0:        monitoring-plugins-old-files-%{version}.tar.bz2
Provides:       nagios-plugins-check_old_files = %{version}-%{release}
Obsoletes:      nagios-plugins-check_old_files < %{version}-%{release}
Requires:       python3
Requires:       python3-docopt
BuildRequires:  nagios-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description

The script monitors presence of the files that have modification time older
than given number of minutes.

%prep
%setup -q

%install
install -D -m755 check_old_files  %{buildroot}/%{nagios_plugindir}/check_old_files

%files
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%doc LICENSE
%{nagios_plugindir}/check_old_files

%changelog
