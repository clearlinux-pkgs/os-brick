#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4F398DEAE440091C (infra-root@openstack.org)
#
Name     : os-brick
Version  : 2.11.0
Release  : 42
URL      : http://tarballs.openstack.org/os-brick/os-brick-2.11.0.tar.gz
Source0  : http://tarballs.openstack.org/os-brick/os-brick-2.11.0.tar.gz
Source1  : http://tarballs.openstack.org/os-brick/os-brick-2.11.0.tar.gz.asc
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
BuildRequires : Babel
BuildRequires : buildreq-distutils3
BuildRequires : eventlet
BuildRequires : os-win
BuildRequires : oslo.concurrency
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.privsep
BuildRequires : oslo.service
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : requests
BuildRequires : retrying
BuildRequires : six
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
%setup -q -n os-brick-2.11.0
cd %{_builddir}/os-brick-2.11.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576569081
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/os-brick
cp %{_builddir}/os-brick-2.11.0/LICENSE %{buildroot}/usr/share/package-licenses/os-brick/294b43b2cec9919063be1a3b49e8722648424779
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
/usr/share/package-licenses/os-brick/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
