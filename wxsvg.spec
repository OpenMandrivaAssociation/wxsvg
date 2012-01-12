%define		major		0
%define		libname		%mklibname %{name} %{major}
%define		develname	%mklibname %{name} -d

Name:		wxsvg
Summary:	A library to create, manipulate and render SVG files
Version:	1.1.5
Release:	1
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		wxsvg-1.1.5-Makefile.am.patch
Patch1:		wxsvg-1.1.5-linkage.patch
URL:		http://wxsvg.sourceforge.net/
License:	wxWidgets
Group:		System/Libraries
BuildRequires:	wxgtku2.8-devel >= 2.8.12
BuildRequires:	libart_lgpl-devel
BuildRequires:	ffmpeg-devel

%description
wxSVG is a C++ library to create, manipulate and render SVG files.

%package -n	%{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{develname}
Summary:	Header files and libraries from %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname wxsvg 0 -d}
Obsoletes:	%{name}-devel

%description -n	%{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
#move files to a better place
mv *.m4 m4/
autoreconf -vfi
%configure2_5x \
	--disable-static \
	--with-wx-config=%{_bindir}/wx-config-unicode \
	--enable-ffmpeg

%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING TODO
%{_bindir}/svgview

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib%{name}.pc
