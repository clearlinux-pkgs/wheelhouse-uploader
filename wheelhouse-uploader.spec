#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wheelhouse-uploader
Version  : 0.10.2
Release  : 13
URL      : https://files.pythonhosted.org/packages/9e/74/5f2263e576f1a34a84782fd58d7eb80bbe2020e22cdfbe7f4881d58e204a/wheelhouse-uploader-0.10.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/9e/74/5f2263e576f1a34a84782fd58d7eb80bbe2020e22cdfbe7f4881d58e204a/wheelhouse-uploader-0.10.2.tar.gz
Summary  : Upload wheels to any cloud storage supported by Libcloud
Group    : Development/Tools
License  : MIT
Requires: wheelhouse-uploader-python = %{version}-%{release}
Requires: wheelhouse-uploader-python3 = %{version}-%{release}
Requires: apache-libcloud
Requires: certifi
Requires: packaging
Requires: setuptools
BuildRequires : apache-libcloud
BuildRequires : buildreq-distutils3
BuildRequires : certifi
BuildRequires : packaging
BuildRequires : setuptools
BuildRequires : setuptools-markdown
Patch1: deps.patch

%description
===================
        
        Upload/download wheels to/from cloud storage using Apache Libcloud.
        Helps package maintainers build wheels for their packages and upload
        them to PyPI.
        
        The cloud storage containers are typically populated by Continuous
        Integration servers that generate and test binary packages on various
        platforms (Windows and OSX for several versions and architectures for
        Python). At release time the project maintainer can collect all the
        generated package for a specific version of the project and upload them
        all at once to PyPI.
        
        Installation
        ------------

%package python
Summary: python components for the wheelhouse-uploader package.
Group: Default
Requires: wheelhouse-uploader-python3 = %{version}-%{release}

%description python
python components for the wheelhouse-uploader package.


%package python3
Summary: python3 components for the wheelhouse-uploader package.
Group: Default
Requires: python3-core
Provides: pypi(wheelhouse_uploader)
Requires: pypi(apache_libcloud)
Requires: pypi(certifi)
Requires: pypi(packaging)
Requires: pypi(setuptools)

%description python3
python3 components for the wheelhouse-uploader package.


%prep
%setup -q -n wheelhouse-uploader-0.10.2
cd %{_builddir}/wheelhouse-uploader-0.10.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583698633
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
