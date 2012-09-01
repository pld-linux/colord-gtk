#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries
%bcond_without	vala		# don't build Vala API
#
Summary:	GTK helper library for colord
Summary(pl.UTF-8):	Biblioteka pomocniczna GTK dla colord
Name:		colord-gtk
Version:	0.1.23
Release:	2
License:	GPL v2+ and LGPL v2+
Group:		Libraries
Source0:	http://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz
# Source0-md5:	019fa6f9349ef39d1bd28c3dcf6fb191
URL:		http://www.freedesktop.org/software/colord/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.9
BuildRequires:	colord-devel >= %{version}
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gobject-introspection-devel >= 0.9.8
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.0
BuildRequires:	lcms2-devel >= 2.2
BuildRequires:	libtool >= 2:2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.644
%if %{with vala}
BuildRequires:	vala
BuildRequires:	vala-colord >= %{version}
%endif
Requires:	colord-libs >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK helper library for colord.

%description -l pl.UTF-8
Biblioteka pomocniczna GTK dla colord.

%package devel
Summary:	Header files for colord-gtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki colord-gtk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	colord-devel >= %{version}
Requires:	gtk+3-devel >= 3.0

%description devel
Header files for colord-gtk library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki colord-gtk.

%package static
Summary:	Static colord-gtk library
Summary(pl.UTF-8):	Statyczna biblioteka colord-gtk
Group:		Development/Libraries
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

%description apidocs
colord-gtk API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API colord-gtk.

%package -n vala-colord-gtk
Summary:	colord-gtk API for Vala language
Summary(pl.UTF-8):	API colord-gtk dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala-colord >= %{version}

%description -n vala-colord-gtk
colord-gtk API for Vala language.

%description -n vala-colord-gtk -l pl.UTF-8
API colord-gtk dla języka Vala.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{__enable_disable apidocs gtk-doc} \
	%{__enable_disable static_libs static} \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

# only empty translation exists atm. (as of 0.1.22)
#find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README TODO
%attr(755,root,root) %{_libdir}/libcolord-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcolord-gtk.so.1
%{_libdir}/girepository-1.0/ColordGtk-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcolord-gtk.so
%{_includedir}/colord-1/colord-gtk.h
%{_includedir}/colord-1/colord-gtk
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
%{_datadir}/vala/vapi/colord-gtk.vapi
%endif
