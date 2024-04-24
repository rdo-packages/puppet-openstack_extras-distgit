%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xf8675126e2411e7748dd46662fc2093e4682645f
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-openstack_extras
Version:        24.0.1
Release:        1%{?dist}
Summary:        Puppet OpenStack Extras Module
License:        ASL 2.0

URL:            https://launchpad.net/puppet-openstack-extras

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

#Requires:       puppet-apt
Requires:       puppet-corosync
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%if 0%{?rhel} > 8
Requires:       rubygem-rexml
%endif

%description
Puppet OpenStack Extras Module

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%setup -q -n openstack-openstack_extras-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/openstack_extras/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/openstack_extras/



%files
%{_datadir}/openstack-puppet/modules/openstack_extras/


%changelog
* Wed Apr 24 2024 RDO <dev@lists.rdoproject.org> 24.0.1-1
- Update to 24.0.1

* Thu Apr 18 2024 RDO <dev@lists.rdoproject.org> 24.0.0-1
- Update to 24.0.0



