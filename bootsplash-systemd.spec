Name:		bootsplash-systemd
Version:	0.1.2
Release:	1
Url:		https://github.com/charveey/bootsplash-systemd
Source0:	https://github.com/charveey/bootsplash-systemd/archive/master/%{name}-%{version}.tar.gz
Summary:	Systemd unit files for controlling in-kernel bootsplash
License:	GPLv2
BuildArch:	noarch

%description
Systemd unit files for controlling in-kernel bootsplash

%prep
%autosetup -p1 -n %{name}-master

%build

%install
mkdir -p %{buildroot}/lib/systemd/system
cp *.path *.service %{buildroot}/lib/systemd/system/

%files
/lib/systemd/system/*.service
/lib/systemd/system/*.path
