#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	prefork
Summary:	prefork - optimize module loading across forking and non-forking scenarios
Summary(pl):	prefork - optymalizacja ³adowania modu³ów dla rozwidlonych i nierozwidlonych scenariuszy
Name:		perl-prefork
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AD/ADAMK/%{pdir}-%{version}.tar.gz
# Source0-md5:	040b340931bd8190b87c81130ea5f8d0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.24-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The prefork pragma is intended to allow module writers to optimise
module loading for both scenarios with as little additional code as
possible.

The prefork.pm is intended to serve as a central and optional
marshalling point for state detection (are we running in procedural or
pre-forking mode) and to act as a relatively light-weight module
loader.

%description -l pl
prefork ma umo¿liwiæ pisz±cym modu³y zoptymalizowanie ³adowania
modu³ów dla obu scenariuszy przy u¿yciu jak najmniejszego dodatkowego
kodu.

prefork.pm ma s³u¿yæ jako centralny i opcjonalnie prowadz±cy punkt dla
wykrywania stanów (czy program dzia³a w trybie proceduralnym, czy
pre-fork) i dzia³aæ jako relatywnie lekki modu³ do wczytywania
modu³ów.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"%{pdir}")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
