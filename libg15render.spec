%define libname %mklibname g15render 1
%define libname_devel %mklibname g15render -d

Name:           libg15render
Version:        1.2
Release:        11
Summary:        Library to render text and shapes into a buffer usable by the G15 keyboard
License:        GPLv2+
Group:          System/Libraries
URL:            http://g15tools.sourceforge.net/
Source0:        http://downloads.sourceforge.net/g15tools/libg15render-%{version}.tar.bz2
BuildRequires:  freetype-devel
BuildRequires:  g15-devel
BuildRequires:  doxygen

%description
This is a library to render text and shapes into a buffer usable by the
Logitech G15 Gaming Keyboard.

This library probably isn't very useful without libg15 and/or g15daemon.

%package -n %{libname}
Summary:        Renders text and shapes into a buffer usable by the G15 keyboard
Group:          System/Libraries
Provides:       g15render = %{EVRD}

%description -n %{libname}
This is a library to render text and shapes into a buffer usable by the
Logitech G15 Gaming Keyboard.

This library probably isn't very useful without libg15 and/or g15daemon.

%package -n %{libname_devel}
Summary:        Renders text and shapes into a buffer usable by the G15 keyboard
Group:          Development/C
Provides:       g15render-devel = %{EVRD}
Requires:       g15render = %{version}

%description -n %{libname_devel}
This is a library to render text and shapes into a buffer usable by the
Logitech G15 Gaming Keyboard.

This library probably isn't very useful without libg15 and/or g15daemon.

%prep
%setup -q

%build
%configure2_5x --enable-ttf --disable-static
%make
%{_bindir}/doxygen

%install
%{makeinstall_std}
rm -r %{buildroot}%{_docdir}

%files -n %{libname}
%defattr(-,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_libdir}/libg15render.so.*
%{_mandir}/man3/*

%files -n %{libname_devel}
%defattr(-,root,root,0755)
%doc doc/html
%{_includedir}/*
%{_libdir}/libg15render.so




