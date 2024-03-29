%define		modname fckeditor
Summary:	Drupal FCKeditor WYSIWYG Editor Module
Summary(pl.UTF-8):	Moduł edytora WYSIWYG FCKeditor dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	5238481c701a9e24ab050b80ef4f53ba
URL:		http://drupal.org/project/fckeditor
Requires:	drupal >= 4.6.0
Requires:	fckeditor
Requires:	webserver(php) >= 4.3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules

%description
This module allows Drupal to replace textarea fields with FCKeditor.

This HTML text editor brings to the web many of the powerful
functionalities of known desktop editors like Word. It's really
lightweight and doesn't require any kind of installation on the client
computer.

%description -l pl.UTF-8
Ten moduł umożliwia Drupalowi zastąpienie pól textarea FCKeditorem.

Ten edytor tekstu HTML udostępnia stronom WWW wiele potężnych funkcji
znanych edytorów biurowych, takich jak Word. Jest naprawdę lekki i nie
wymaga żadnej inicjalizacji na komputerze klienckim.

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_moddir}/{lib,ssip}}
install *.module $RPM_BUILD_ROOT%{_moddir}
cp -a lib/* $RPM_BUILD_ROOT%{_moddir}/lib
cp -a ssip/* $RPM_BUILD_ROOT%{_moddir}/ssip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_moddir}/*.module
%{_moddir}/lib
%{_moddir}/ssip
