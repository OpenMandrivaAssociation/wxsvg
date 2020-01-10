%define		major		3
%define		libname		%mklibname %{name} %{major}
%define		develname	%mklibname %{name} -d

Name:		wxsvg
Summary:	A library to create, manipulate and render SVG files
Version:	1.5.4
Release:	1
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
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
%autopatch -p1

%build
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


%changelog
* Tue Jul 03 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.1.9-1
+ Revision: 807974
- update to 1.1.9

* Sun Jun 03 2012 Andrey Bondrov <abondrov@mandriva.org> 1.1.8-1
+ Revision: 802137
- New version 1.1.8

  + Alexander Khrukin <akhrukin@mandriva.org>
    - *.la files removed

* Mon Feb 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.6-1
+ Revision: 778138
- version update 1.1.6

* Thu Jan 12 2012 Andrey Bondrov <abondrov@mandriva.org> 1.1.5-1
+ Revision: 760354
- New version 1.1.5, drop RPM4 stuff

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 615464
- the mass rebuild of 2010.1 packages

* Mon Apr 26 2010 Emmanuel Andry <eandry@mandriva.org> 1.0.3-1mdv2010.1
+ Revision: 539310
- New version 1.0.3

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.0-1mdv2010.0
+ Revision: 445840
- rebuild

* Fri Dec 05 2008 Götz Waschk <waschk@mandriva.org> 1.0-1mdv2009.1
+ Revision: 310552
- new version
- drop patch
- build with wxGTK 2.8

* Wed Oct 15 2008 Adam Williamson <awilliamson@mandriva.org> 1.0-0.beta11.2mdv2009.1
+ Revision: 293803
- rebuild for new ffmpeg major

* Sat Sep 06 2008 Adam Williamson <awilliamson@mandriva.org> 1.0-0.beta11.1mdv2009.0
+ Revision: 281875
- slightly streamline file list
- drop unnecessary devel provide
- add a missing indefinite article to the description...
- replace headercheck.patch with includes.patch: the ffmpeg stuff is now
  broken in a new and excitingly different way
- drop unnecessary defines (and completely wrong release, where'd that come
  from? good thing it didn't get pushed)
- new release 1.0beta11

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Thu Jun 12 2008 Adam Williamson <awilliamson@mandriva.org> 1.0-0.beta10.2mdv2009.0
+ Revision: 218571
- doh, do the removal in the right place...
- drop svgui and calculette as they don't actually work: see
  http://sourceforge.net/forum/forum.php?thread_id=2069902&forum_id=424987
- use angle brackets not quotation marks for the includes in headercheck.patch (anssi)

* Thu Jun 12 2008 Adam Williamson <awilliamson@mandriva.org> 1.0-0.beta10.1mdv2009.0
+ Revision: 218564
- protect major in file list
- workaround lack of ltmain.sh in source
- now buildrequires ffmpeg-devel
- correct license using new policy
- add headercheck.patch: fix ffmpeg detection and flags for our version and
  layout of ffmpeg-devel
- drop freetype-fix.patch: removing the entire original file and then recreating
  it is not the correct way to make a "patch"...according to changelog this
  was introduced to fix build with newer freetype, but it builds fine against
  current freetype without the patch, so whatever the problem was, likely fixed
  upstream
- new devel policy
- spec clean
- new release 1.0 beta 10

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 1.0-0.beta7.3mdv2008.1
+ Revision: 140933
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Feb 24 2007 Emmanuel Andry <eandry@mandriva.org> 1.0-0.beta7.3mdv2007.0
+ Revision: 125328
- switch back to wxGTK2.6, dvdstyler doesn't support 2.8

* Wed Jan 24 2007 Emmanuel Andry <eandry@mandriva.org> 1.0-0.beta7.2mdv2007.1
+ Revision: 113052
- rebuild against wxGTK2.8

* Wed Jan 24 2007 Emmanuel Andry <eandry@mandriva.org> 1.0-0.beta7.1mdv2007.1
+ Revision: 112799
- buildrequires libart_lgpl-devel
- New version 1.0 beta 7
  diff patch to fix build with latest freetype

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Import wxsvg

* Wed Apr 12 2006 Jerome Martin <jmartin@mandriva.org> 1.0-0.beta6.1mdk
- beta6
- Fixed licence

* Fri Feb 03 2006 Austin Acton <austin@mandriva.org> 1.0-0.beta5.1mdk
- beta5 + fixes from cvs

* Fri Dec 30 2005 Austin Acton <austin@mandriva.org> 1.0-0.beta4.1mdk
- initial package

