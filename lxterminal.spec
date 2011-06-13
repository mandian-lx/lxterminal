%define git 1
%define prerel 31813de
%define gitday 20110613
%define ver 0.1.9

Summary:	Lightweight VTE-based terminal emulator
Name:     	lxterminal
%if %git
Version:	%{ver}.git%{gitday}
Source0:	%{name}-%{prerel}.tar.gz
%else
Version:	%{ver}
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
%endif
Release:	%mkrel 4
License:	GPLv2+
Group:		Graphical desktop/Other
Patch0:		lxterminal-0.1.9-fix-build-with-new-vte.patch
Patch1:		lxterminal-deprecate-revert.patch
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
%if %git
BuildRequires:	docbook-to-man docbook-dtd412-xml
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
%patch1 -p0 -b.deprecate_revert
%else
%setup -q -n %{name}
%patch0 -p1 -b .vte
%endif
#%patch1 -p1 -b .dragndrop

%build
%if %git
./autogen.sh
%configure2_5x --enable-man
%else
%configure2_5x
%endif
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%post  

%postun

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_mandir}/man1/*
