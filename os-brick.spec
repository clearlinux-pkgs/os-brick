#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : os-brick
Version  : 2.8.0
Release  : 34
URL      : http://tarballs.openstack.org/os-brick/os-brick-2.8.0.tar.gz
Source0  : http://tarballs.openstack.org/os-brick/os-brick-2.8.0.tar.gz
Source99 : http://tarballs.openstack.org/os-brick/os-brick-2.8.0.tar.gz.asc
Summary  : OpenStack Cinder brick library for managing local volume attaches
Group    : Development/Tools
License  : Apache-2.0
Requires: os-brick-data = %{version}-%{release}
Requires: os-brick-license = %{version}-%{release}
Requires: os-brick-python = %{version}-%{release}
Requires: os-brick-python3 = %{version}-%{release}
Requires: Babel
Requires: eventlet
Requires: os-win
Requires: oslo.concurrency
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.privsep
Requires: oslo.service
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: retrying
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
Patch1: 0001-move-etc-os-brick-rootwrap.d-os-brick.filters-to-sta.patch

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/os-brick.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package data
Summary: data components for the os-brick package.
Group: Data

%description data
data components for the os-brick package.


%package license
Summary: license components for the os-brick package.
Group: Default

%description license
license components for the os-brick package.


%package python
Summary: python components for the os-brick package.
Group: Default
Requires: os-brick-python3 = %{version}-%{release}

%description python
python components for the os-brick package.


%package python3
Summary: python3 components for the os-brick package.
Group: Default
Requires: python3-core

%description python3
python3 components for the os-brick package.


%prep
%setup -q -n os-brick-2.8.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552016773
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/os-brick
cp LICENSE %{buildroot}/usr/share/package-licenses/os-brick/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/defaults/os-brick/rootwrap.d/os-brick.filters

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/os-brick/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
