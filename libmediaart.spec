Name:           libmediaart
Version:        1.9.4
Release:        1%{?dist}
Summary:        Library for managing media art caches

License:        LGPLv2+
URL:            https://github.com/curlybeast/libmediaart
Source0:        https://download.gnome.org/sources/%{name}/1.9/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(glib-2.0) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%if 0%{?fedora} || 0%{?rhel} > 7
# Test requires the jpeg gdk-pixbuf loader
BuildRequires:  gdk-pixbuf2-modules
%endif
BuildRequires:  vala vala-devel
BuildRequires:  dbus

%description
Library tasked with managing, extracting and handling media art caches.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package  tests
Summary:  Tests for the %{name} package
Group:    Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%setup -q


%build
%configure --disable-static \
  --enable-gdkpixbuf \
  --disable-qt \
  --enable-installed-tests
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete -print

%check
dbus-run-session -- make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING.LESSER
%doc AUTHORS NEWS
%{_libdir}/libmediaart-2.0.so.*
%{_libdir}/girepository-1.0/MediaArt-2.0.typelib

%files devel
%{_includedir}/libmediaart-2.0
%{_libdir}/libmediaart-2.0.so
%{_libdir}/pkgconfig/libmediaart-2.0.pc
%{_datadir}/gir-1.0/MediaArt-2.0.gir
%{_datadir}/gtk-doc/html/libmediaart
%{_datadir}/vala/vapi/libmediaart-2.0.vapi

%files tests
%{_libexecdir}/installed-tests/libmediaart
%{_datadir}/installed-tests


%changelog
* Fri May 25 2018 Kalev Lember <klember@redhat.com> - 1.9.4-1
- Update to 1.9.4
- Resolves: #1570009

* Thu Mar 09 2017 Kalev Lember <klember@redhat.com> - 1.9.1-1
- Update to 1.9.1
- Drop upstreamed patches
- Resolves: #1387011

* Thu Oct 20 2016 Kalev Lember <klember@redhat.com> - 1.9.0-1
- Update to 1.9.0
- Resolves: #1387011

* Mon Sep 22 2014 Yanko Kaneti <yaneti@declera.com> - 0.7.0-1
- Update to 0.7.0

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.4.0-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr  1 2014 Yanko Kaneti <yaneti@declera.com> - 0.4.0-1
- Update to 0.4.0

* Fri Mar  7 2014 Yanko Kaneti <yaneti@declera.com> - 0.3.0-1
- Update to 0.3.0. Drop upstreamed patches.

* Sat Feb  8 2014 Yanko Kaneti <yaneti@declera.com> - 0.2.0-4
- Add patches to avoid unnecessary linkage

* Sat Feb  8 2014 Yanko Kaneti <yaneti@declera.com> - 0.2.0-3
- Incorporate most changes suggested in the review (#1062686)

* Fri Feb  7 2014 Yanko Kaneti <yaneti@declera.com> - 0.2.0-2
- Qt can be ignored, its only there for systems without gdk-pixbuf

* Fri Feb  7 2014 Yanko Kaneti <yaneti@declera.com> - 0.2.0-1
- Initial attempt
