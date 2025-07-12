#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	C library for reading virtual slides
Summary(pl.UTF-8):	Biblioteka C do odczytu wirtualnych slajdów
Name:		openslide
Version:	4.0.0
Release:	2
License:	LGPL v2.1
Group:		Libraries
#Source0Download: https://github.com/openslide/openslide/releases/
Source0:	https://github.com/openslide/openslide/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	d2e8222659f5a17f22168f846277db14
URL:		https://openslide.org/
BuildRequires:	cairo-devel >= 1.2
BuildRequires:	gdk-pixbuf2-devel >= 2.14
BuildRequires:	glib2-devel >= 1:2.56
BuildRequires:	libdicom-devel >= 1.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.2.1
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson >= 0.53
BuildRequires:	ninja >= 1.5
BuildRequires:	openjpeg2-devel >= 2.1.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sqlite3-devel >= 3.6.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	cairo >= 1.2
Requires:	gdk-pixbuf2 >= 2.14
Requires:	glib2 >= 1:2.56
Requires:	libdicom >= 1.0.0
Requires:	libpng >= 2:1.2.1
Requires:	openjpeg2 >= 2.1.0
Requires:	sqlite3 >= 3.6.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.

%description -l pl.UTF-8
Biblioteka OpenSlide pozwala programom na dostęp do plików wirtualnych
slajdów niezależnie od ich formatu.

%package devel
Summary:	Header files for OpenSlide library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenSlide
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for OpenSlide library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenSlide.

%package static
Summary:	Static OpenSlide library
Summary(pl.UTF-8):	Statyczna biblioteka OpenSlide
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenSlide library.

%description static -l pl.UTF-8
Statyczna biblioteka OpenSlide.

%package apidocs
Summary:	API documentation for OpenSlide library
Summary(pl.UTF-8):	Dokumentacja API biblioteki OpenSlide
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for OpenSlide library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki OpenSlide.

%package tools
Summary:	Command line tools for working with virtual slides
Summary(pl.UTF-8):	Narzędzia linii poleceń do pracy z wirtualnymi slajdami
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description tools
Command line tools for working with virtual slides.

%description tools -l pl.UTF-8
Narzędzia linii poleceń do pracy z wirtualnymi slajdami.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library=shared}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_libdir}/libopenslide.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenslide.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenslide.so
%{_includedir}/openslide
%{_pkgconfigdir}/openslide.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libopenslide.a
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/openslide-quickhash1sum
%attr(755,root,root) %{_bindir}/openslide-show-properties
%attr(755,root,root) %{_bindir}/openslide-write-png
%attr(755,root,root) %{_bindir}/slidetool
%{_mandir}/man1/openslide-quickhash1sum.1*
%{_mandir}/man1/openslide-show-properties.1*
%{_mandir}/man1/openslide-write-png.1*
%{_mandir}/man1/slidetool.1*

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
