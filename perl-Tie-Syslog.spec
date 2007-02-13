#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# require resolvable hostname and syslog access
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	Syslog
Summary:	Tie::Syslog Perl module - tie a filehandle to Syslog
Summary(pl.UTF-8):	Moduł Perla Tie::Syslog - związanie uchwytu pliku z logiem systemowym
Name:		perl-Tie-Syslog
Version:	1.07
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8afc88e3ffe0bd64fdcde58a827a23dc
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to tie a filehandle (output only) to syslog.
This becomes useful in general when you want to capture any activity
that happens on STDERR and see that it is syslogged for later perusal.
You can also create an arbitrary filehandle, say LOG, and send stuff
to syslog by printing to this filehandle. This module depends on the
Sys::Syslog module to actually get info to syslog.

%description -l pl.UTF-8
Ten moduł pozwala powiązać uchwyt pliku (tylko wyjściowy) z logiem
systemowym. Jest to przydatne jeśli potrzeba wychwycić każdą aktywność
na standardowym wyjściu błędu i zachować do późniejszej analizy. Można
także utworzyć dowolny uchwyt pliku, np. LOG, i wysyłać komunikaty do
sysloga poprzez pisanie do tego uchwytu. Ten moduł przy wysyłaniu
informaji do loga systemowego polega na module Sys::Syslog.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
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
%doc Changes README
%{perl_vendorlib}/Tie/Syslog.pm
%{_mandir}/man3/*
