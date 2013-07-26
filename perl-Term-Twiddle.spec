%define upstream_name    Term-Twiddle
%define upstream_version 2.73

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 2.73
Release:	1

Summary:	Twiddles baton while-u-wait for long subrout
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Term/Term-Twiddle-2.73.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Time::HiRes)
BuildArch:	noarch

%description
Always fascinated by the spinner during FreeBSD's loader bootstrap, I
wanted to capture it so I could view it any time I wanted to--and I wanted
to make other people find that same joy I did. Now, anytime you or your
users have to wait for something to finish, instead of twiddling their
thumbs, they can watch the computer twiddle its thumbs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test </dev/null

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 2.710.0-2mdv2011.0
+ Revision: 655224
- rebuild for updated spec-helper

* Thu Dec 31 2009 Jérôme Quelin <jquelin@mandriva.org> 2.710.0-1mdv2011.0
+ Revision: 484420
- import perl-Term-Twiddle


* Thu Dec 31 2009 cpan2dist 2.71-1mdv
- initial mdv release, generated with cpan2dist

