%define		status		stable
%define		pearname	Horde_Date
Summary:	%{pearname} - Horde Date package
Name:		php-horde-Horde_Date
Version:	1.0.11
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	ff48ed46c8bfd4817fa7590ba0a5eb72
URL:		https://github.com/horde/horde/tree/master/framework/Date/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.593
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Nls < 2.0.0
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-calendar
Suggests:	php-horde-Horde_Icalendar
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Icalendar.*)

%description
Package for creating and manipulating dates.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Date.php
%{php_pear_dir}/Horde/Date
%{php_pear_dir}/data/Horde_Date
