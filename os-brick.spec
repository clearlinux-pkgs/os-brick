#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB9069B1335700CDC (infra-root@openstack.org)
#
Name     : os-brick
Version  : 1.11.0
Release  : 23
URL      : http://tarballs.openstack.org/os-brick/os-brick-1.11.0.tar.gz
Source0  : http://tarballs.openstack.org/os-brick/os-brick-1.11.0.tar.gz
Source99 : http://tarballs.openstack.org/os-brick/os-brick-1.11.0.tar.gz.asc
Summary  : OpenStack Cinder brick library for managing local volume attaches
Group    : Development/Tools
License  : Apache-2.0
Requires: os-brick-python
Requires: os-brick-data
Requires: Babel
Requires: eventlet
Requires: os-win
Requires: oslo.concurrency
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.serialization
Requires: oslo.service
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: retrying
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: 0001-move-etc-os-brick-rootwrap.d-os-brick.filters-to-sta.patch

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/os-brick.svg
:target: http://governance.openstack.org/reference/tags/index.html

%package data
Summary: data components for the os-brick package.
Group: Data

%description data
data components for the os-brick package.


%package python
Summary: python components for the os-brick package.
Group: Default

%description python
python components for the os-brick package.


%prep
%setup -q -n os-brick-1.11.0
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489852691
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489852691
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/defaults/os-brick/rootwrap.d/os-brick.filters

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
