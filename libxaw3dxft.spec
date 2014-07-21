#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Extended version of Xaw3d widgets library
Summary(pl.UTF-8):	Rozszerzona wersja biblioteki widgetów Xaw3d
Name:		libxaw3dxft
Version:	1.3.3
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/sf-xpaint/%{name}-%{version}.tar.bz2
# Source0-md5:	d0bafeae76f3e50dbdce3e91bd149697
Patch0:		%{name}-link.patch
Patch1:		%{name}-pkgconfdir.patch
URL:		http://sourceforge.net/projects/sf-xpaint/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel
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
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Xaw3dxft library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Xaw3dxft.

%package static
Summary:	Static Xaw3dxft library
Summary(pl.UTF-8):	Statyczna biblioteka Xaw3dxft
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Xaw3dxft library.

%description static -l pl.UTF-8
Statyczna biblioteka Xaw3dxft.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
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
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libXaw3dxft.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXaw3dxft.so.7

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libXaw3dxft.so
%{_includedir}/X11/Xaw3dxft
%{_pkgconfigdir}/libxaw3dxft.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libXaw3dxft.a
%endif
