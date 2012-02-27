#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Extended version of Xaw3d
#Summary(pl.UTF-8):	-
Name:		libxaw3dxft
Version:	1.3.3
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/sf-xpaint/%{name}-%{version}.tar.bz2
# Source0-md5:	d0bafeae76f3e50dbdce3e91bd149697
Patch0:		%{name}-link.patch
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
Xaw3dxft is an extended version of xaw3d with support for UTF8 input
and UTF8 encoding of text, and rendering text with the Freetype
library and Truetype fonts. It should be mostly compatible with the
original xaw3d library, except for font management : everything using
the old X11 core font routines should be replaced by their freetype
equivalents.

#%description -l pl.UTF-8

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

%prep
%setup -q
%patch0 -p1

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

%{__mv} $RPM_BUILD_ROOT/usr/lib/pkgconfig $RPM_BUILD_ROOT%{_libdir}

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
%{_pkgconfigdir}/%{name}.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libXaw3dxft.a
%endif
