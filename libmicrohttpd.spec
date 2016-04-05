#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmicrohttpd
Version  : 0.9.48
Release  : 1
URL      : http://ftp.gnu.org/gnu/libmicrohttpd/libmicrohttpd-0.9.48.tar.gz
Source0  : http://ftp.gnu.org/gnu/libmicrohttpd/libmicrohttpd-0.9.48.tar.gz
Summary  : A library for creating an embedded HTTP server
Group    : Development/Tools
License  : GFDL-1.3 LGPL-2.1
Requires: libmicrohttpd-lib
Requires: libmicrohttpd-doc
BuildRequires : curl-dev
BuildRequires : gnutls
BuildRequires : libgcrypt-dev
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
Requires: libmicrohttpd-lib
Provides: libmicrohttpd-devel

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

%description lib
lib components for the libmicrohttpd package.


%prep
%setup -q -n libmicrohttpd-0.9.48

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
