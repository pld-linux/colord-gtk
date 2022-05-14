#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	static_libs	# static libraries
%bcond_without	gtk2		# additional GTK+ 2.x version of library
%bcond_without	gtk4		# additional GTK 4 version of library
%bcond_without	vala		# Vala API

%define	colord_ver	0.1.27
Summary:	GTK helper library for colord
Summary(pl.UTF-8):	Biblioteka pomocniczna GTK dla colord
Name:		colord-gtk
Version:	0.3.0
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (cd-convert utility)
Group:		X11/Libraries
Source0:	https://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz
# Source0-md5:	08c245d6482b3923a2b6a09f7fbbe612
URL:		https://www.freedesktop.org/software/colord/
BuildRequires:	colord-devel >= %{colord_ver}
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gobject-introspection-devel >= 0.9.8
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2.0}
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	gtk-doc >= 1.9
%{?with_gtk4:BuildRequires:	gtk4-devel >= 4.4}
BuildRequires:	lcms2-devel >= 2.2
BuildRequires:	meson >= 0.46.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sed >= 4.0
%if %{with vala}
BuildRequires:	vala
BuildRequires:	vala-colord >= %{colord_ver}
%endif
Requires:	colord-libs >= %{colord_ver}
Requires:	glib2 >= 1:2.28.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK helper library for colord.

%description -l pl.UTF-8
Biblioteka pomocniczna GTK dla colord.

%package headers
Summary:	Header files for colord-gtk libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek colord-gtk
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	colord-devel >= %{colord_ver}
Requires:	glib2-devel >= 1:2.28.0
Conflicts:	colord-gtk-devel < 0.3

%description headers
Header files for colord-gtk libraries.

%description headers -l pl.UTF-8
Pliki nagłówkowe bibliotek colord-gtk.

%package devel
Summary:	Development files for colord-gtk library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki colord-gtk
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-headers = %{version}-%{release}
Requires:	colord-devel >= %{colord_ver}
Requires:	glib2-devel >= 1:2.28.0
Requires:	gtk+3-devel >= 3.0

%description devel
Development files for colord-gtk library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki colord-gtk.

%package static
Summary:	Static colord-gtk library
Summary(pl.UTF-8):	Statyczna biblioteka colord-gtk
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static colord-gtk library.

%description static -l pl.UTF-8
Statyczna biblioteka colord-gtk.

%package apidocs
Summary:	colord-gtk API documentation
Summary(pl.UTF-8):	Dokumentacja API colord-gtk
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
colord-gtk API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API colord-gtk.

%package -n vala-colord-gtk
Summary:	colord-gtk API for Vala language
Summary(pl.UTF-8):	API colord-gtk dla języka Vala
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala-colord >= %{colord_ver}
BuildArch:	noarch

%description -n vala-colord-gtk
colord-gtk API for Vala language.

%description -n vala-colord-gtk -l pl.UTF-8
API colord-gtk dla języka Vala.

%package -n colord-gtk2
Summary:	GTK 2 helper library for colord
Summary(pl.UTF-8):	Biblioteka pomocniczna GTK 2 dla colord
Group:		X11/Libraries
Requires:	colord-libs >= %{colord_ver}
Requires:	glib2 >= 1:2.28.0

%description -n colord-gtk2
GTK 2 helper library for colord.

%description -n colord-gtk2 -l pl.UTF-8
Biblioteka pomocniczna GTK 2 dla colord.

%package -n colord-gtk2-devel
Summary:	Development files for colord-gtk2 library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki colord-gtk2
Group:		X11/Development/Libraries
Requires:	%{name}-headers = %{version}-%{release}
Requires:	colord-gtk2 = %{version}-%{release}
Requires:	gtk+2-devel >= 2.0

%description -n colord-gtk2-devel
Development files for colord-gtk2 library.

%description -n colord-gtk2-devel -l pl.UTF-8
Pliki programistyczne biblioteki colord-gtk2.

%package -n colord-gtk2-static
Summary:	Static colord-gtk2 library
Summary(pl.UTF-8):	Statyczna biblioteka colord-gtk2
Group:		X11/Development/Libraries
Requires:	colord-gtk2-devel = %{version}-%{release}

%description -n colord-gtk2-static
Static colord-gtk2 library.

%description -n colord-gtk2-static -l pl.UTF-8
Statyczna biblioteka colord-gtk2.

%package -n colord-gtk4
Summary:	GTK 4 helper library for colord
Summary(pl.UTF-8):	Biblioteka pomocniczna GTK 4 dla colord
Group:		X11/Libraries
Requires:	colord-libs >= %{colord_ver}
Requires:	glib2 >= 1:2.28.0
Requires:	gtk4 >= 4.4

%description -n colord-gtk4
GTK 4 helper library for colord.

%description -n colord-gtk4 -l pl.UTF-8
Biblioteka pomocniczna GTK 4 dla colord.

%package -n colord-gtk4-devel
Summary:	Development files for colord-gtk4 library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki colord-gtk4
Group:		X11/Development/Libraries
Requires:	%{name}-headers = %{version}-%{release}
Requires:	colord-gtk4 = %{version}-%{release}
Requires:	gtk4-devel >= 4.4

%description -n colord-gtk4-devel
Development files for colord-gtk4 library.

%description -n colord-gtk4-devel -l pl.UTF-8
Pliki programistyczne biblioteki colord-gtk4.

%package -n colord-gtk4-static
Summary:	Static colord-gtk4 library
Summary(pl.UTF-8):	Statyczna biblioteka colord-gtk4
Group:		X11/Development/Libraries
Requires:	colord-gtk4-devel = %{version}-%{release}

%description -n colord-gtk4-static
Static colord-gtk4 library.

%description -n colord-gtk4-static -l pl.UTF-8
Statyczna biblioteka colord-gtk4.

%prep
%setup -q

%if %{with static_libs}
%{__sed} -i -e 's/ = shared_library/ = library/' libcolord-gtk/meson.build
%endif

%build
%meson build \
	-Dgtk2=true \
	%{!?with_gtk4:-Dgtk4=false} \
	-Dvapi=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# only empty translation exists atm. (as of 0.1.26)
#find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n colord-gtk2 -p /sbin/ldconfig
%postun	-n colord-gtk2 -p /sbin/ldconfig

%post	-n colord-gtk4 -p /sbin/ldconfig
%postun	-n colord-gtk4 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README TODO
%attr(755,root,root) %{_bindir}/cd-convert
%attr(755,root,root) %{_libdir}/libcolord-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcolord-gtk.so.1
%{_libdir}/girepository-1.0/ColordGtk-1.0.typelib
%{_mandir}/man1/cd-convert.1*

%files headers
%defattr(644,root,root,755)
%{_includedir}/colord-1/colord-gtk.h
%{_includedir}/colord-1/colord-gtk

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcolord-gtk.so
%{_datadir}/gir-1.0/ColordGtk-1.0.gir
%{_pkgconfigdir}/colord-gtk.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcolord-gtk.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/colord-gtk
%endif

%if %{with vala}
%files -n vala-colord-gtk
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/colord-gtk.deps
%{_datadir}/vala/vapi/colord-gtk.vapi
%endif

%if %{with gtk2}
%files -n colord-gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcolord-gtk2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcolord-gtk2.so.1

%files -n colord-gtk2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcolord-gtk2.so
%{_pkgconfigdir}/colord-gtk2.pc

%if %{with static_libs}
%files -n colord-gtk2-static
%defattr(644,root,root,755)
%{_libdir}/libcolord-gtk2.a
%endif
%endif

%if %{with gtk4}
%files -n colord-gtk4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcolord-gtk4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcolord-gtk4.so.1

%files -n colord-gtk4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcolord-gtk4.so
%{_pkgconfigdir}/colord-gtk4.pc

%if %{with static_libs}
%files -n colord-gtk4-static
%defattr(644,root,root,755)
%{_libdir}/libcolord-gtk4.a
%endif
%endif
