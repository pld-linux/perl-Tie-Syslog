%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	Syslog
Summary:	Tie::Syslog - Tie a filehandle to Syslog.
Name:		perl-Tie-Syslog
Version:	1.07
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to tie a filehandle (output only) to syslog. This
becomes useful in general when you want to capture any activity that
happens on STDERR and see that it is syslogged for later perusal. You can
also create an arbitrary filehandle, say LOG, and send stuff to syslog
by printing to this filehandle. This module depends on the Sys::Syslog
module to actually get info to syslog.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Tie/Syslog.pm
%{_mandir}/man3/*
