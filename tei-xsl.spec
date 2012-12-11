%define Name tei-xsl
%define Version 5.2.16
%define Release 2

Name:		%{Name}
Version:	%{Version}
Release:	%{Release}
Group       	: Publishing

Summary     	: Sebastian Rahtz's modular stylesheets for TEI

License   	: Artistic like
URL         	: http://www.tei-c.org/Stylesheets/teixsl.html

Obsoletes:	TEI-style-html
Provides:	TEI-style-html
Requires:	TEI-DTD
Requires(Pre):	sgml-common

# ZIP spurce downloadable at http://sourceforge.net/project/showfiles.php?group_id=106328&package_id=141124
Source0		: %{name}-%{Version}.tar.bz2
BuildArch	: noarch

%define sgmlbase %{_datadir}/sgml/ 

%Description
These XSL stylesheets allow to convert any TEI document
to the HTML, FO and LaTeX formats.

%prep
%setup

%build


%install
DESTDIR=$RPM_BUILD_ROOT%{sgmlbase}/TEI/xsl-stylesheets-%{Version}
mkdir -p $DESTDIR
cp -a p4 p5 $DESTDIR

ln -sf xsl-stylesheets-%{Version} \
	$RPM_BUILD_ROOT%{sgmlbase}/TEI/xsl-stylesheets

# Catalogs management left for brave packagers.

%files
%defattr (-,root,root)
%doc doc/*
%{sgmlbase}/TEI/*

%changelog 
* Wed Mar 22 2006 Camille Begnis <camille@mandriva.com> 5.2.16-1mdk
- Now includes various output formats in 5.2.16

* Mon Sep  6 2004 Camille Begnis <camille@mandrakesoft.com> 2.0-3mdk
- rebuild

* Fri Aug 29 2003  <camille@ke.mandrakesoft.com> 2.0-2mdk
- add missing dir

* Mon Jul 21 2003  <camille@ke.mandrakesoft.com> 2.0-1mdk
- First specs for MDK

