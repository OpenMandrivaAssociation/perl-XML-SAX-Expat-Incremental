%define upstream_name    XML-SAX-Expat-Incremental
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    XML::SAX::Expat subclass for non-blocking parsing, with XML::Parser::ExpatNB
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires: perl(XML::SAX::Expat)
BuildRequires: perl(Test::Exception)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
XML::SAX::Expat subclass for non-blocking (incremental) parsing, with 
XML::Parser::ExpatNB .


%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
