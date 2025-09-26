#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Extended version of Xaw3d widgets library
Summary(pl.UTF-8):	Rozszerzona wersja biblioteki widgetów Xaw3d
Name:		libxaw3dxft
Version:	1.6.4
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://github.com/DaveFlater/libXaw3dXft/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	57130fb9ce5c9b7011635286011e890d
URL:		http://sourceforge.net/projects/sf-xpaint/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xaw3dxft is an extended version of Xaw3d widgets library with support
for UTF-8 input and UTF-8 encoding of text, and rendering text with
the FreeType library and TrueType fonts. It should be mostly
compatible with the original Xaw3d library, except for font
management: everything using the old X11 core font routines should be
replaced by their FreeType equivalents.

%description -l pl.UTF-8
Xaw3dxft to rozszerzona wersja Xaw3d z obsługą wejścia UTF-8,
kodowaniem tekstu UTF-8 oraz renderowaniem tekstu przy użyciu
biblioteki FreeType z fontami TrueType. Powinna być w większości
zgodna z oryginalną biblioteką Xaw3d z wyjątkiem zarządzania fontami:
wszystko wykorzystujące stare procedury obsługi fontów X11 powinny być
zastąpione odpowiednikami wykorzystującymi z FreeType.

%package devel
Summary:	Header files for Xaw3dxft library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Xaw3dxft
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fontconfig-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXft-devel
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXt-devel

%description devel
Header files for Xaw3dxft library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Xaw3dxft.

%package static
Summary:	Static Xaw3dxft library
Summary(pl.UTF-8):	Statyczna biblioteka Xaw3dxft
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Xaw3dxft library.

%description static -l pl.UTF-8
Statyczna biblioteka Xaw3dxft.

%prep
%setup -q -n libXaw3dXft-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-arrow-scrollbars \
	--enable-gray-stipples \
	--enable-multiplane-pixmaps \
	%{!?with_static_libs:--disable-static}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXaw3dxft.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/libXaw3dxft.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXaw3dxft.so.8

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXaw3dxft.so
%{_includedir}/X11/Xaw3dxft
%{_pkgconfigdir}/libxaw3dxft.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libXaw3dxft.a
%endif
