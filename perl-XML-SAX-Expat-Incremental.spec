%define upstream_name    XML-SAX-Expat-Incremental
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	XML::SAX::Expat subclass for non-blocking parsing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(XML::SAX::Expat)
BuildRequires:	perl(Test::Exception)
BuildArch:	noarch

%description
XML::SAX::Expat subclass for non-blocking (incremental) parsing, with 
XML::Parser::ExpatNB .


%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# test fails, key verification problem
rm -f t/dist.t

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 658558
- rebuild for updated spec-helper

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 406253
- rebuild using %%perl_convert_version

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.05-4mdv2009.0
+ Revision: 258880
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.05-3mdv2009.0
+ Revision: 246783
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2008.1
+ Revision: 97580
- update to new version 0.05

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.04-3mdv2008.0
+ Revision: 23492
- rebuild


* Sat Apr 22 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-2mdk
- Add BuildRequires

* Wed Apr 19 2006 Michael Scherer <misc@mandriva.org> 0.04-1mdk
- First Mandriva package

