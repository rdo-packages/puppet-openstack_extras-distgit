%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-openstack_extras
Version:        XXX
Release:        XXX
Summary:        Puppet OpenStack Extras Module
License:        ASL 2.0

URL:            https://launchpad.net/puppet-openstack-extras

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

#Requires:       puppet-apt
Requires:       puppet-corosync
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Puppet OpenStack Extras Module

%prep
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


# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/puppet-openstack_extras/commit/?id=3754a9ff7c6f5e34906179d97132f9f6844bf2cd
