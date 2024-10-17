%define version 2.24.1
%define release 3

%define pkgname	gtkmm-documentation
%define api_version 2.4

Name:		gtkmm%{api_version}-documentation
Summary:	GTKmm reference manual and examples
Version:	%{version}
Release:	%{release}
License:	GPLv2+ and GFDL
Group:		Books/Other
URL:		https://gtkmm.sourceforge.net/
Source0:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
source1:		.abf.yml
BuildRequires: pkgconfig(gtkmm-2.4) >= 2.24.0
BuildRequires: glibmm2.4-devel >= 2.24.0
BuildRequires: libglademm2.4-devel >= 2.6.0
BuildRequires: pkgconfig(gnome-doc-utils)
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

%find_lang gtkmm-tutorial --with-gnome || touch gtkmm-tutorial.lang
#gw already in gtkmm2.4-doc
rm -rf %buildroot%{_datadir}/doc/gtkmm-%{api_version}/docs/{FAQ,images}

%files -f gtkmm-tutorial.lang
%defattr(-, root, root)
%doc %{_datadir}/doc/gtkmm-%{api_version}




%changelog
* Mon Apr 16 2012 Götz Waschk <waschk@mandriva.org> 2.24.1-2mdv2012.0
+ Revision: 791262
- yearly rebuild

* Fri Apr 15 2011 Götz Waschk <waschk@mandriva.org> 2.24.1-1
+ Revision: 653100
- update to new version 2.24.1

* Mon Apr 04 2011 Götz Waschk <waschk@mandriva.org> 2.24.0-1
+ Revision: 650226
- new version
- bump gtk dep

* Thu Oct 28 2010 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2011.0
+ Revision: 589745
- update to new version 2.22.0

* Tue Sep 21 2010 Götz Waschk <waschk@mandriva.org> 2.21.8.1-1mdv2011.0
+ Revision: 580382
- update to new version 2.21.8.1

* Tue Apr 13 2010 Götz Waschk <waschk@mandriva.org> 2.20.1-1mdv2010.1
+ Revision: 534014
- update to new version 2.20.1

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2010.1
+ Revision: 529946
- new version
- bump deps

* Thu Feb 11 2010 Götz Waschk <waschk@mandriva.org> 2.19.3-1mdv2010.1
+ Revision: 504284
- update to new version 2.19.3

* Tue Jan 19 2010 Götz Waschk <waschk@mandriva.org> 2.19.2-1mdv2010.1
+ Revision: 493567
- update to new version 2.19.2

* Mon Sep 28 2009 Götz Waschk <waschk@mandriva.org> 2.17.4-1mdv2010.0
+ Revision: 450608
- update to new version 2.17.4

* Tue Sep 15 2009 Götz Waschk <waschk@mandriva.org> 2.17.3-1mdv2010.0
+ Revision: 443159
- update to new version 2.17.3

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 2.17.1-1mdv2010.0
+ Revision: 440840
- new version
- update file list

* Mon Sep 07 2009 Götz Waschk <waschk@mandriva.org> 2.17.0-1mdv2010.0
+ Revision: 432755
- new version
- disable parallel make

* Tue Mar 17 2009 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2009.1
+ Revision: 356704
- update to new version 2.16.0

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 2.14.0-1mdv2009.0
+ Revision: 286614
- new version
- update file list
- update license
- import gtkmm2.4-doc

