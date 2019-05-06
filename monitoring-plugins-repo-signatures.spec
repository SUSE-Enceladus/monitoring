#
# spec file for package monitoring-plugins-repo-signatures
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

Name:           monitoring-plugins-repo-signatures
Version:        20190330
Release:        0
Summary:        Check mirrored repository metadata signature validity
License:        GPL-2.0
Group:          System/Monitoring
Url:            https://github.com/SUSE-Enceladus/monitoring
Source0:        monitoring-plugins-repo-signatures-%{version}.tar.bz2
Provides:       nagios-plugins-repo-signatures = %{version}-%{release}
Obsoletes:      nagios-plugins-repo-signatures < %{version}-%{release}
BuildRequires:  nagios-rpm-macros
BuildArch:      noarch

%description
The script verifies that repository metadata has valid signatures.

%prep
%setup -q

%install
install -D -m755 check_repo_signatures %{buildroot}/%{nagios_plugindir}/check_repo_signatures

%files
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%doc LICENSE
%{nagios_plugindir}/check_repo_signatures

%changelog
