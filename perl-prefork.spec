#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	prefork
Summary:	prefork - optimize module loading across forking and non-forking scenarios
Summary(pl.UTF-8):	prefork - optymalizacja ładowania modułów dla rozwidlonych i nierozwidlonych scenariuszy
Name:		perl-prefork
Version:	1.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/E/ET/ETHER/%{pdir}-%{version}.tar.gz
# Source0-md5:	60d97a66a1e6e4ccfa51f8662a511048
URL:		https://metacpan.org/release/prefork
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.24-2
%if %{with tests}
BuildRequires:	perl-Scalar-List-Utils >= 0.18
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
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

%description -l pl.UTF-8
prefork ma umożliwić piszącym moduły zoptymalizowanie ładowania
modułów dla obu scenariuszy przy użyciu jak najmniejszego dodatkowego
kodu.

prefork.pm ma służyć jako centralny i opcjonalnie prowadzący punkt dla
wykrywania stanów (czy program działa w trybie proceduralnym, czy
pre-fork) i działać jako relatywnie lekki moduł do wczytywania
modułów.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
#rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/prefork/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/prefork.pm
%{_mandir}/man3/prefork.3pm*
