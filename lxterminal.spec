Summary:	Lightweight VTE-based terminal emulator
Name:     	lxterminal
Version:	0.1.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel vte-devel

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
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post  

%postun

%files -f %{name}.lang
%defattr(-, root, root)
%{_sbindir}/%name
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
