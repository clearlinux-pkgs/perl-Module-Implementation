#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-Implementation
Version  : 0.09
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Module-Implementation-0.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Module-Implementation-0.09.tar.gz
Summary  : 'Loads one of several alternate underlying implementations for a module'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Module-Implementation-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(Try::Tiny)

%description
# NAME
Module::Implementation - Loads one of several alternate underlying implementations for a module

%package dev
Summary: dev components for the perl-Module-Implementation package.
Group: Development
Provides: perl-Module-Implementation-devel = %{version}-%{release}

%description dev
dev components for the perl-Module-Implementation package.


%package license
Summary: license components for the perl-Module-Implementation package.
Group: Default

%description license
license components for the perl-Module-Implementation package.


%prep
%setup -q -n Module-Implementation-0.09

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Module-Implementation
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Module-Implementation/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Module/Implementation.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::Implementation.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Module-Implementation/LICENSE
