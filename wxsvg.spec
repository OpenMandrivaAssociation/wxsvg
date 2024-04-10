%global	Werror_cflags %{nil}

%define	libname %mklibname %{name}
%define	devname %mklibname %{name} -d

Summary:	A library to create, manipulate and render SVG files
Name:		wxsvg
Version:	1.5.24
Release:	3
License:	wxWidgets
Group:		System/Libraries
Url:		http://wxsvg.sourceforge.net/
Source0:	https://downloads.sourceforge.net/project/wxsvg/wxsvg/%{version}/wxsvg-%{version}.tar.bz2
Patch0:		wxsvg-1.5.24-clang.patch
Patch1:		wxsvg-1.5.24-ffmpeg7.patch
BuildRequires:	ffmpeg-devel
BuildRequires:	wxgtku3.2-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(pangocairo)

%description
wxSVG is a C++ library to create, manipulate and render SVG files.

%files
%license COPYING
%doc AUTHORS ChangeLog TODO
%{_bindir}/svgview

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}.

%files -n %{libname}
%license COPYING
%doc AUTHORS ChangeLog TODO
%{_libdir}/lib%{name}.so.*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Header files and libraries from %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%files -n %{devname}
%license COPYING
%doc AUTHORS ChangeLog TODO
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
#Move files to a better place
#mv *.m4 m4/

%configure \
	--disable-static \
	--with-wx-config="%{_bindir}/wx-config" \
	--enable-ffmpeg
%make


%install
%make_install

