%define version 2.22.0
%define release %mkrel 1

%define pkgname	gtkmm-documentation
%define api_version 2.4

Name:		gtkmm%{api_version}-documentation
Summary:	GTKmm reference manual and examples
Version:	%{version}
Release:	%{release}
License:	GPLv2+ and GFDL
Group:		Books/Other
URL:		http://gtkmm.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
BuildRequires: gtkmm2.4-devel >= 2.20.0
BuildRequires: glibmm2.4-devel >= 2.24.0
BuildRequires: libglademm2.4-devel >= 2.6.0
BuildRequires: gnome-doc-utils
BuildArch: noarch
Requires: gtkmm2.4-doc >= 2.14.0

%description
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains all API documentation for gtkmm. You can readily read
this documentation with devhelp, a documentation reader.

%prep
%setup -q -n %{pkgname}-%{version}

%build
./configure --prefix=%_prefix
make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang gtkmm-tutorial --with-gnome
#gw already in gtkmm2.4-doc
rm -rf %buildroot%{_datadir}/doc/gtkmm-%{api_version}/docs/{FAQ,images}

%clean
rm -rf %{buildroot}

%files -f gtkmm-tutorial.lang
%defattr(-, root, root)
%doc %{_datadir}/doc/gtkmm-%{api_version}


