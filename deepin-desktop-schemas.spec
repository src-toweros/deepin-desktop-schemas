Name:           deepin-desktop-schemas
Version:        5.5.0.6
Release:        2
Summary:        GSettings deepin desktop-wide schemas
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-desktop-schemas
Source0:        %{name}_%{version}.orig.tar.xz

BuildArch:      noarch
BuildRequires:  python3 golang-bin
BuildRequires:  glib2
#add jzy
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
export GOPATH=%{_builddir}/%{name}-%{version}/vendor
%make_build

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
* Wed Aug 19 2020 chenbo pan <panchenbo@uniontech.com> - 5.5.0.6-2
- remove golang devel
* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.5.0.6-1
- Package init
