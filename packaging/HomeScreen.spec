Name:       HomeScreen
Summary:    An app launching application
Version:    0.0.1
Release:    1
Group:      Applications/System
License:    Apache 2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  common-apps
BuildRequires:  zip
BuildRequires:  desktop-file-utils
Requires: pkgmgr
Requires: crosswalk
Requires: tizen-extensions-crosswalk
Requires: pkgmgr-server
Requires: model-config-ivi
Requires: tizen-middleware-units
Requires: tizen-platform-config

%description
A proof of concept pure html5 UI

%prep
%setup -q -n %{name}-%{version}

%build
make wgtPkg

%install
rm -rf %{buildroot}
make install_obs "OBS=1" DESTDIR="%{?buildroot}"

%post
su app -c "pkgcmd -i -t wgt -p /opt/usr/apps/.preinstallWidgets/JLRPOCX001.HomeScreen.wgt -q"

%postun
su app -c "pkgcmd -u -n JLRPOCX001 -q"

%files
%defattr(-,root,root,-)
/opt/usr/apps/.preinstallWidgets/JLRPOCX001.HomeScreen.wgt

