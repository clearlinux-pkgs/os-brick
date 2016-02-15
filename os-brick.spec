#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : os-brick
Version  : 0.8.0
Release  : 9
URL      : http://tarballs.openstack.org/os-brick/os-brick-0.8.0.tar.gz
Source0  : http://tarballs.openstack.org/os-brick/os-brick-0.8.0.tar.gz
Summary  : OpenStack Cinder brick library for managing local volume attaches
Group    : Development/Tools
License  : Apache-2.0
Requires: os-brick-python
Requires: os-brick-data
BuildRequires : Sphinx-python
BuildRequires : coverage-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : hacking
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : oslo.config
BuildRequires : oslo.serialization-python
BuildRequires : oslo.service-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : repoze.lru-python
BuildRequires : requests-python
BuildRequires : retrying-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : wrapt-python
Patch1: 0001-move-etc-os-brick-rootwrap.d-os-brick.filters-to-sta.patch

%description
===============================
brick
===============================
.. image:: https://img.shields.io/pypi/v/os-brick.svg
:target: https://pypi.python.org/pypi/os-brick/
:alt: Latest Version

%package data
Summary: data components for the os-brick package.
Group: Data

%description data
data components for the os-brick package.


%package python
Summary: python components for the os-brick package.
Group: Default
Requires: oslo.serialization-python
Requires: oslo.service-python
Requires: oslo.utils-python
Requires: requests-python
Requires: retrying-python
Requires: six-python

%description python
python components for the os-brick package.


%prep
%setup -q -n os-brick-0.8.0
%patch1 -p1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose py2 || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/defaults/os-brick/rootwrap.d/os-brick.filters

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
