%define realname   XML-SAX-Expat-Incremental

Name:		perl-%{realname}
Version:    0.05
Release:    %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:    XML::SAX::Expat subclass for non-blocking parsing, with XML::Parser::ExpatNB
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-SAX-Expat-Incremental-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRequires:	perl-devel
BuildRequires: perl(XML::SAX::Expat)
BuildRequires: perl(Test::Exception)
BuildArch: noarch

%description
XML::SAX::Expat subclass for non-blocking (incremental) parsing, with 
XML::Parser::ExpatNB .


%prep
%setup -q -n XML-SAX-Expat-Incremental-%{version} 
# test fails, key verification problem
rm -f t/dist.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{perl_vendorlib}/*
%{_mandir}/man3/*

