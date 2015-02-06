%define upstream_name    ExtUtils-Install
%define upstream_version 1.68

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(VMS::Filespec\\)'
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Yet another framework for writing test scripts



License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Compare)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildArch:	noarch

%description
*STOP!* If you're just getting started writing tests, have a look at
Test::Simple first. This is a drop in replacement for Test::Simple which
you can switch to once you get the hang of basic testing.

The purpose of this module is to provide a wide range of testing utilities.
Various ways to say "ok" with better diagnostics, facilities to skip tests,
test future features and compare complicated data structures. While you can
do almost anything with a simple 'ok()' function, it doesn't provide good
diagnostic output.

I love it when a plan comes together
    Before anything else, you need a testing plan. This basically declares
    how many tests your script is going to run to protect against premature
    failure.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*





