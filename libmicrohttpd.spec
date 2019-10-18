#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x939E6BE1E29FC3CC (grothoff@gnu.org)
#
Name     : libmicrohttpd
Version  : 0.9.67
Release  : 22
URL      : https://mirrors.kernel.org/gnu/libmicrohttpd/libmicrohttpd-0.9.67.tar.gz
Source0  : https://mirrors.kernel.org/gnu/libmicrohttpd/libmicrohttpd-0.9.67.tar.gz
Source1 : https://mirrors.kernel.org/gnu/libmicrohttpd/libmicrohttpd-0.9.67.tar.gz.sig
Summary  : a small C library that is supposed to make it easy to run an HTTP server as part of another application.
Group    : Development/Tools
License  : LGPL-2.1
Requires: libmicrohttpd-lib = %{version}-%{release}
Requires: libmicrohttpd-license = %{version}-%{release}
BuildRequires : curl-dev
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
Requires: libmicrohttpd = %{version}-%{release}

%description dev
dev components for the libmicrohttpd package.


%package doc
Summary: doc components for the libmicrohttpd package.
Group: Documentation

%description doc
doc components for the libmicrohttpd package.


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
%setup -q -n libmicrohttpd-0.9.67

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571405937
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1571405937
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libmicrohttpd
cp %{_builddir}/libmicrohttpd-0.9.67/COPYING %{buildroot}/usr/share/package-licenses/libmicrohttpd/8a7f857077114c00b2777664d804a6afaa93049f
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/microhttpd.h
/usr/lib64/libmicrohttpd.so
/usr/lib64/pkgconfig/libmicrohttpd.pc
/usr/share/man/man3/libmicrohttpd.3

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmicrohttpd.so.12
/usr/lib64/libmicrohttpd.so.12.54.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmicrohttpd/8a7f857077114c00b2777664d804a6afaa93049f
