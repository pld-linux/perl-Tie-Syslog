%define	pdir	Tie
%define	pnam	Syslog
%include	/usr/lib/rpm/macros.perl
Summary:	Tie-Syslog perl module
Summary(pl):	Modu� perla Tie-Syslog
Name:		perl-Tie-Syslog
Version:	1.07
Release:	2

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-Syslog perl module.

%description -l pl
Modu� perla Tie-Syslog.

%prep
%setup -q -n Tie-Syslog-%{version}

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
