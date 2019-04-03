#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0A5B101836580288 (georg@python.org)
#
Name     : deprecated-Pygments
Version  : 2.2.0
Release  : 49
URL      : http://pypi.debian.net/Pygments/Pygments-2.2.0.tar.gz
Source0  : http://pypi.debian.net/Pygments/Pygments-2.2.0.tar.gz
Source99 : http://pypi.debian.net/Pygments/Pygments-2.2.0.tar.gz.asc
Summary  : Pygments is a syntax highlighting package written in Python.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: deprecated-Pygments-bin = %{version}-%{release}
Requires: deprecated-Pygments-license = %{version}-%{release}
Requires: deprecated-Pygments-python = %{version}-%{release}
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : buildreq-qmake
BuildRequires : nose

%description
===================
This is the source of Pygments.  It is a generic syntax highlighter that
supports over 300 languages and text formats, for use in code hosting, forums,
wikis or other applications that need to prettify source code.

%package bin
Summary: bin components for the deprecated-Pygments package.
Group: Binaries
Requires: deprecated-Pygments-license = %{version}-%{release}

%description bin
bin components for the deprecated-Pygments package.


%package legacypython
Summary: legacypython components for the deprecated-Pygments package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-Pygments package.


%package license
Summary: license components for the deprecated-Pygments package.
Group: Default

%description license
license components for the deprecated-Pygments package.


%package python
Summary: python components for the deprecated-Pygments package.
Group: Default
Provides: deprecated-pygments-python

%description python
python components for the deprecated-Pygments package.


%prep
%setup -q -n Pygments-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554326148
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-Pygments
cp LICENSE %{buildroot}/usr/share/package-licenses/deprecated-Pygments/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pygmentize

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-Pygments/LICENSE

%files python
%defattr(-,root,root,-)
