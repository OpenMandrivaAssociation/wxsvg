%define name	wxsvg
%define version	1.0
%define beta	7
%define release %mkrel 0.beta%{beta}.3

%define major	0
%define libname %mklibname %name %major

Name: 	 	%{name}
Summary: 	A library to create, manipulate and render SVG files
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}b%{beta}.tar.bz2
Patch0:		wxsvg-freetype-fix.patch
URL:		http://wxsvg.sourceforge.net/
License:	LGPL
Group:		System/Libraries
BuildRequires:	wxGTK2.6-devel libart_lgpl-devel

%description
wxSVG is C++ library to create, manipulate and render SVG files.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries
#Provides:	%name
#Obsoletes:	%name = %version-%release

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q -n %name-%{version}b%{beta}
%patch0

%build
./autogen.sh
%configure2_5x --with-wx-config=%_bindir/wx-config-ansi 
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING TODO
%{_bindir}/svgview

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


