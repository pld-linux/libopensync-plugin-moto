Summary:	OpenSync plugin for syncing to a Motorola mobile phone
Summary(pl.UTF-8):	Wtyczka do OpenSync synchronizująca z telefonami komórkowymi Motoroli
Name:		libopensync-plugin-moto
Version:	0.22
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	255f2eb991579bcbcc971ab25e58127b
URL:		http://www.opensync.org/
BuildRequires:	sed >= 4.0
Requires:	libopensync-plugin-python >= %{version}
Requires:	python-dateutil
Requires:	python-pybluez
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync Plugin for syncing with Motorola phones using the AT command
set.

%description -l pl.UTF-8
Wtyczka do OpenSync służąca do synchronizacji z telefonami firmy
Motorola przy użyciu zbioru poleceń AT.

%prep
%setup -q
%{__sed} -i -e '1s,#!.*python,#!%{__python},' mototool

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/opensync/python-plugins,%{_datadir}/opensync/defaults}
install motosync.py $RPM_BUILD_ROOT%{_libdir}/opensync/python-plugins
cp -a moto-sync $RPM_BUILD_ROOT%{_datadir}/opensync/defaults

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/opensync/python-plugins/motosync.py
%{_datadir}/opensync/defaults/moto-sync
