%define upstream_name    Term-Twiddle
%define upstream_version 2.71

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Twiddles baton while-u-wait for long subrout
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Time::HiRes)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Always fascinated by the spinner during FreeBSD's loader bootstrap, I
wanted to capture it so I could view it any time I wanted to--and I wanted
to make other people find that same joy I did. Now, anytime you or your
users have to wait for something to finish, instead of twiddling their
thumbs, they can watch the computer twiddle its thumbs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test </dev/null

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


