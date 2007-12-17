%define Name tei-xsl
%define Version 5.2.16
%define Release 1mdk

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
Requires(Pre):	sgml-common >= 0.6.3-2mdk


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
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT%{sgmlbase}/TEI/xsl-stylesheets-%{Version}
mkdir -p $DESTDIR
cp -a p4 p5 $DESTDIR

ln -sf xsl-stylesheets-%{Version} \
	$RPM_BUILD_ROOT%{sgmlbase}/TEI/xsl-stylesheets

%clean
rm -rf $RPM_BUILD_ROOT

# Catalogs management left for brave packagers.

%files
%defattr (-,root,root)
%doc doc/*
%dir %{sgmlbase}/TEI/xsl-stylesheets-%{Version}
%{sgmlbase}/TEI/
%{sgmlbase}/TEI/xsl-stylesheets

