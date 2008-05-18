Summary:	OpenSync plugin for syncing to a Motorola mobile phone
Summary(pl.UTF-8):	Wtyczka do OpenSync synchronizująca z telefonami komórkowymi Motoroli
Name:		libopensync-plugin-moto
Version:	0.36
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://opensync.org/download/releases/0.36/libopensync-plugin-moto-0.36.tar.bz2
# Source0-md5:	8dcecd4afb87e4645a152194fd3b5e55
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
install -d $RPM_BUILD_ROOT{%{_libdir}/opensync-1.0/python-plugins,%{_datadir}/opensync-1.0/defaults}
install motosync.py $RPM_BUILD_ROOT%{_libdir}/opensync-1.0/python-plugins
cp -a moto-sync $RPM_BUILD_ROOT%{_datadir}/opensync-1.0/defaults

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/opensync-1.0/python-plugins/motosync.py
%{_datadir}/opensync-1.0/defaults/moto-sync
