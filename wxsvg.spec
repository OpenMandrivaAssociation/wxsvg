%define version	1.0
%define beta	10
%define release %mkrel 0.beta%{beta}.2

%define major		0
%define libname		%mklibname %name %major
%define develname	%mklibname %name -d

Name: 	 	wxsvg
Summary: 	A library to create, manipulate and render SVG files
Version: 	1.0
Release: 	%{release}
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}b%{beta}.tar.gz
#Patch0:		wxsvg-freetype-fix.patch
Patch0:		wxsvg-1.0b10-headercheck.patch
URL:		http://wxsvg.sourceforge.net/
License:	wxWidgets
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	wxGTK2.6-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	ffmpeg-devel

%description
wxSVG is C++ library to create, manipulate and render SVG files.

%package -n 	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{develname}
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname wxsvg 0 -d}
Obsoletes: 	%{name}-devel

%description -n %{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q -n %{name}-%{version}b%{beta}
#%patch0
%patch0 -p1 -b .headercheck

%build
# automake doesn't work without ltmain.sh... - AdamW 2008/06
ln -s %{_datadir}/libtool/ltmain.sh .

./autogen.sh
%configure2_5x --with-wx-config=%{_bindir}/wx-config-ansi 
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

# these don't actually work - see http://sourceforge.net/forum/forum.php?thread_id=2069902&forum_id=424987
# - AdamW 2008/06
rm -f %{_bindir}/svgui
rm -f %{_bindir}/calculette

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING TODO
%{_bindir}/svgview

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


