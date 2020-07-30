Name:           deepin-desktop-schemas
Version:        5.5.0.6
Release:        1
Summary:        GSettings deepin desktop-wide schemas
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-desktop-schemas
Source0:        %{name}_%{version}.orig.tar.xz

BuildArch:      noarch
BuildRequires:  python3 golang-bin
BuildRequires:  glib2
#add jzy
BuildRequires:  go-lib-devel
Requires:       dconf
Requires:       deepin-gtk-theme
Requires:       deepin-icon-theme
Requires:       deepin-sound-theme
Obsoletes:      deepin-artwork-themes <= 15.12.4

%description
%{summary}.

%prep
%setup -q

sed -i '/picture-uri/s|default_background.jpg|default.png|' \
    overrides/common/com.deepin.wrap.gnome.desktop.override
sed -i 's|python|python3|' Makefile tools/overrides.py

%build
export GOPATH=/usr/share/gocode
%make_build ARCH=x86

%install
%make_install PREFIX=%{_prefix}

%check
make test

%files
%doc README.md
%license LICENSE
%{_datadir}/glib-2.0/schemas/*
/usr/share/deepin-app-store/*
/usr/share/deepin-desktop-schemas/*
/usr/share/deepin-appstore/*


%changelog
* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.5.0.6-1
- Package init
