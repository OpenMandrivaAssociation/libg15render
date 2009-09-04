%define libname %mklibname g15render 1
%define libname_devel %mklibname g15render -d
%define libname_static_devel %mklibname g15render -d -s

Name:           libg15render
Version:        1.2
Release:        %mkrel 6
Summary:        Library to render text and shapes into a buffer usable by the G15 keyboard
License:        GPL
Group:          System/Libraries
URL:            http://g15tools.sourceforge.net/
Source:         http://downloads.sourceforge.net/g15tools/libg15render-%{version}.tar.bz2
BuildRequires:  freetype2-devel
BuildRequires:  g15-devel
BuildRequires:  doxygen
BuildRequires:  tetex-latex
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This is a library to render text and shapes into a buffer usable by the
Logitech G15 Gaming Keyboard.

This library probably isn't very useful without libg15 and/or g15daemon.

%package -n %{libname}
Summary:        Renders text and shapes into a buffer usable by the G15 keyboard
Group:          System/Libraries
Provides:       g15render = %{version}-%{release}

%description -n %{libname}
This is a library to render text and shapes into a buffer usable by the
Logitech G15 Gaming Keyboard.

This library probably isn't very useful without libg15 and/or g15daemon.

%package -n %{libname_devel}
Summary:        Renders text and shapes into a buffer usable by the G15 keyboard
Group:          Development/C
Provides:       g15render-devel = %{version}-%{release}
Requires:       g15render = %{version}-%{release}

%description -n %{libname_devel}
This is a library to render text and shapes into a buffer usable by the
Logitech G15 Gaming Keyboard.

This library probably isn't very useful without libg15 and/or g15daemon.

%package -n %{libname_static_devel}
Summary:        Renders text and shapes into a buffer usable by the G15 keyboard
Group:          Development/C
Provides:       g15render-static-devel = %{version}-%{release}
Requires:       g15render-devel = %{version}-%{release}

%description -n %{libname_static_devel}
This is a library to render text and shapes into a buffer usable by the
Logitech G15 Gaming Keyboard.

This library probably isn't very useful without libg15 and/or g15daemon.

%prep
%setup -q

%build
%{configure2_5x} --enable-ttf
%{make}
%{_bindir}/doxygen
pushd doc/latex
%{make} pdf
popd

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} -r %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_libdir}/libg15render.so.*
%{_mandir}/man3/*

%files -n %{libname_devel}
%defattr(-,root,root,0755)
%doc doc/html doc/latex/refman.pdf
%{_includedir}/*
%{_libdir}/lib*.la
%{_libdir}/libg15render.so

%files -n %{libname_static_devel}
%defattr(-,root,root,0755)
%{_libdir}/libg15render*.a
