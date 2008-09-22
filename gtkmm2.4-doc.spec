%define version 2.13.2
%define release %mkrel 1

%define pkgname	gtkmm-documentation
%define api_version 2.4

Name:		gtkmm%{api_version}-doc
Summary:	GTKmm documentation
Version:	%{version}
Release:	%{release}
License:	GPLv2+ and GFDL
Group:		Books/Other
URL:		http://gtkmm.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
BuildRequires: gtkmm2.4-devel >= 2.10.0
BuildRequires: libglademm2.4-devel >= 2.6.0
BuildArch: noarch

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
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang gtkmm-tut-with-examples --with-gnome

%clean
rm -rf %{buildroot}

%files -f gtkmm-tut-with-examples.lang
%defattr(-, root, root)
%doc %{_datadir}/doc/gtkmm-%{api_version}


