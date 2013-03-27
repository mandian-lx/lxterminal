%define git 0
%define prerel 31813de
%define gitday 20110613
%define ver 0.1.11

Summary:	Lightweight VTE-based terminal emulator
Name:     	lxterminal
%if %git
Version:	%{ver}.git%{gitday}
Source0:	%{name}-%{prerel}.tar.gz
%else
Version:	%{ver}
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
%endif
Release:	3
License:	GPLv2+
Group:		Graphical desktop/Other
#Patch0:		lxterminal-0.1.9-fix-build-with-new-vte.patch
#Patch1:		lxterminal-deprecate-revert.patch
Patch2:		mdk-lxterminal-conf.patch
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
%if %git
BuildRequires:	docbook-to-man docbook-dtd412-xml docbook-style-xsl
%endif
BuildRequires:	gtk+2-devel vte-devel
BuildRequires:	intltool

%description
Desktop-independent VTE-based terminal emulator without any unnecessary
dependencies.
 
Feature:
* Support Multi-tab.
* It doesn't have any unnecessary dependencies.
* All instances share the same process to reduce memory usage.
* It has correct behavior with nice performance when resizing window,
  tab and VTE stuff.
* Using unix-socket instead of D-bus to accomplish all instances share
  the same process.

%prep
%if %git
%setup -q -n %{name}-%{prerel}
#patch1 -p0 -b.deprecate_revert
%else
%setup -q -n %{name}-%{version}
#patch0 -p1 -b .vte
%endif
#patch1 -p1 -b .dragndrop
%patch2 -p0 -b.conf

%build
%if %git
./autogen.sh
%configure2_5x --enable-man
%else
%configure2_5x
%endif
%make

%install
%makeinstall_std

%{find_lang} %{name}


%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_mandir}/man1/*


%changelog
* Wed Aug 03 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.11-1mdv2011.0
+ Revision: 692991
- update to 0.1.11

* Mon Jun 13 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.9.git20110613-4
+ Revision: 684465
- fix lxterminal default customisations
- new git snapshot. Fix lxterminal window errors

* Sat Apr 30 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.9-2
+ Revision: 661020
- add patch for drag_and_drop support

* Thu Sep 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.1.9-1mdv2011.0
+ Revision: 575530
- update to 0.1.9
- add patch from upstream to make it build with latest vte

* Mon Jul 19 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.1.8-1mdv2011.0
+ Revision: 555006
- update to 0.1.8

* Mon Mar 01 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.1.7-1mdv2010.1
+ Revision: 513285
- new upstream release 0.1.7

* Mon Jul 13 2009 Funda Wang <fwang@mandriva.org> 0.1.6-1mdv2010.0
+ Revision: 395471
- new version 0.1.6

* Wed Jun 10 2009 Götz Waschk <waschk@mandriva.org> 0.1.5-3mdv2010.0
+ Revision: 384691
- rebuild for new vte

* Tue Jun 02 2009 Götz Waschk <waschk@mandriva.org> 0.1.5-2mdv2010.0
+ Revision: 382167
- rebuild for new libvte

* Sat May 23 2009 Funda Wang <fwang@mandriva.org> 0.1.5-1mdv2010.0
+ Revision: 378898
- New version 0.1.5

* Fri Dec 26 2008 Funda Wang <fwang@mandriva.org> 0.1.4-1mdv2009.1
+ Revision: 319294
- new version 0.1.4

* Tue Dec 16 2008 Funda Wang <fwang@mandriva.org> 0.1.3-2mdv2009.1
+ Revision: 314828
- add upstream patch to rebuild with new flags

* Sat Jun 28 2008 Funda Wang <fwang@mandriva.org> 0.1.3-1mdv2009.0
+ Revision: 229717
- New version 0.1.3

* Sat Jun 21 2008 Funda Wang <fwang@mandriva.org> 0.1.2-1mdv2009.0
+ Revision: 227652
- BR intltool
- import lxterminal


