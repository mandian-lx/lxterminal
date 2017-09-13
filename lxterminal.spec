Summary:	Lightweight VTE-based terminal emulator
Name:		lxterminal
Version:	0.3.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://wiki.lxde.org/en/LXTerminal
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
Patch2:		mdk-lxterminal-conf.patch

BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	pkgconfig(vte)
BuildRequires:	docbook-to-man
BuildRequires:	docbook-style-xsl
BuildRequires:	xsltproc

Requires:	termcap

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

LXTerminal is the standard terminal emulator of LXDE. The terminal is a
desktop-independent VTE-based terminal emulator for LXDE without any
unnecessary dependency.

LXTerminal supports multiple tabs. All instances of program share the same
process to reduce memory usage.
 
Some features:

  * Support Multi-tab.
  * It doesn't have any unnecessary dependencies.
  * All instances share the same process to reduce memory usage.
  * It has correct behavior with nice performance when resizing window,
    tab and VTE stuff.
  * Using unix-socket instead of D-bus to accomplish all instances share
    the same process.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*

#---------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

# locales
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

