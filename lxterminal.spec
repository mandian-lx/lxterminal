%define ver 0.1.11

Summary:	Lightweight VTE-based terminal emulator
Name:		lxterminal
Version:	0.1.11
Release:	5
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
Patch2:		mdk-lxterminal-conf.patch
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	pkgconfig(vte)

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
%setup -qn %{name}-%{version}
%patch2 -p0 -b.conf

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_mandir}/man1/*

