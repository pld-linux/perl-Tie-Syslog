%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	Syslog
Summary:	Tie::Syslog - Tie a filehandle to Syslog
Summary(pl):	Modu� Tie::Syslog - wi���cy uchwyt pliku z logiem systemowym
Name:		perl-Tie-Syslog
Version:	1.07
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8afc88e3ffe0bd64fdcde58a827a23dc
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Ten modu� pozwala powi�za� uchwyt pliku (tylko wyj�ciowy) z logiem
systemowym. Jest to przydatne je�li potrzeba wychwyci� ka�d� aktywno��
na standardowym wyj�ciu b��du i zachowa� do p�niejszej analizy. Mo�na
tak�e utworzy� dowolny uchwyt pliku, np. LOG, i wysy�a� komunikaty do
sysloga poprzez pisanie do tego uchwytu. Ten modu� przy wysy�aniu
informaji do loga systemowego polega na module Sys::Syslog.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tie/Syslog.pm
%{_mandir}/man3/*