#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x460A317C3326D2AE (k2k@narod.ru)
#
Name     : libmicrohttpd
Version  : 0.9.75
Release  : 32
URL      : https://mirrors.kernel.org/gnu/libmicrohttpd/libmicrohttpd-0.9.75.tar.gz
Source0  : https://mirrors.kernel.org/gnu/libmicrohttpd/libmicrohttpd-0.9.75.tar.gz
Source1  : https://mirrors.kernel.org/gnu/libmicrohttpd/libmicrohttpd-0.9.75.tar.gz.sig
Summary  : A library for creating an embedded HTTP server
Group    : Development/Tools
License  : LGPL-2.1
Requires: libmicrohttpd-info = %{version}-%{release}
Requires: libmicrohttpd-lib = %{version}-%{release}
Requires: libmicrohttpd-license = %{version}-%{release}
BuildRequires : file-dev
BuildRequires : gnutls-dev
BuildRequires : grep
BuildRequires : libgcrypt-dev
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(zlib)
BuildRequires : texinfo

%description
About
=====
GNU libmicrohttpd is a GNU package offering a C library that provides
a compact API and implementation of an HTTP 1.1 web server (HTTP 1.0
is also supported).  GNU libmicrohttpd only implements the HTTP 1.1
protocol.  The main application must still provide the application
logic to generate the content.

%package dev
Summary: dev components for the libmicrohttpd package.
Group: Development
Requires: libmicrohttpd-lib = %{version}-%{release}
Provides: libmicrohttpd-devel = %{version}-%{release}
Requires: libmicrohttpd = %{version}-%{release}

%description dev
dev components for the libmicrohttpd package.


%package info
Summary: info components for the libmicrohttpd package.
Group: Default

%description info
info components for the libmicrohttpd package.


%package lib
Summary: lib components for the libmicrohttpd package.
Group: Libraries
Requires: libmicrohttpd-license = %{version}-%{release}

%description lib
lib components for the libmicrohttpd package.


%package license
Summary: license components for the libmicrohttpd package.
Group: Default

%description license
license components for the libmicrohttpd package.


%prep
%setup -q -n libmicrohttpd-0.9.75
cd %{_builddir}/libmicrohttpd-0.9.75

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640621461
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
%configure --disable-static --disable-curl
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1640621461
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libmicrohttpd
cp %{_builddir}/libmicrohttpd-0.9.75/COPYING %{buildroot}/usr/share/package-licenses/libmicrohttpd/8a7f857077114c00b2777664d804a6afaa93049f
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/microhttpd.h
/usr/lib64/libmicrohttpd.so
/usr/lib64/pkgconfig/libmicrohttpd.pc
/usr/share/man/man3/libmicrohttpd.3

%files info
%defattr(0644,root,root,0755)
/usr/share/info/libmicrohttpd-tutorial.info
/usr/share/info/libmicrohttpd.info
/usr/share/info/libmicrohttpd_performance_data.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmicrohttpd.so.12
/usr/lib64/libmicrohttpd.so.12.60.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmicrohttpd/8a7f857077114c00b2777664d804a6afaa93049f
