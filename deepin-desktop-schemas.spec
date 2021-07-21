Name:           deepin-desktop-schemas
Version:        5.8.0.26
Release:        2
Summary:        GSettings deepin desktop-wide schemas
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-desktop-schemas
Source0:        %{name}-%{version}.tar.xz
Source1:	vendor.tar.gz

Provides:       deepin-default-gsettings
Obsoletes:      deepin-default-gsettings

BuildArch:     noarch

BuildRequires:  golang
BuildRequires:  glib2
BuildRequires:  python3 golang-bin
BuildRequires:  deepin-desktop-server

Requires:  deepin-desktop-server

%description
deepin-desktop-schemas contains a collection of GSettings schemas for
 settings shared by various components of a desktop.

%prep
%autosetup
tar -xf %{SOURCE1}

%build
export GOPATH=%{_builddir}/%{name}-%{version}/vendor


%if %{_arch} == "aarch64"
%define  buildarch arm
%else
%define  buildarch x86
%endif

%make_build ARCH=%{buildarch}
%install
%make_install PREFIX=%{_prefix} ARCH=%{buildarch}

%check
make test

%post
data_dir=/usr/share/deepin-desktop-schemas
gschemas_dir=/usr/share/glib-2.0/schemas
app_store_dir=/usr/share/deepin-app-store
app_store_ini_file=$app_store_dir/settings.ini
app_store_ini_file_pro=$app_store_dir/settings-pro.ini
app_store_ini_file_community=$app_store_dir/settings-community.ini
app_store_ini_file_personal=$app_store_dir/settings-personal.ini

SYSTYPE=$(grep Type= /etc/deepin-version|cut -d= -f 2)
product_override_file=$gschemas_dir/91_deepin_product.gschema.override
if [ -e $app_store_ini_file -a -L $app_store_ini_file ]; then
    # delete it if it is symbol link
    rm $app_store_ini_file
fi
case "$SYSTYPE" in
    Professional)
        ln -sf $data_dir/pro-override $product_override_file
        if [ ! -f $app_store_ini_file ]; then
            ln -sf $app_store_ini_file_pro $app_store_ini_file
        fi
    ;;
    Server)
        ln -sf $data_dir/server-override $product_override_file
        if [ ! -f $app_store_ini_file ]; then
            ln -sf $app_store_ini_file_pro $app_store_ini_file
        fi
    ;;
    Desktop)
        ln -sf $data_dir/desktop-override $product_override_file
        if [ ! -f $app_store_ini_file ]; then
            ln -sf $app_store_ini_file_community $app_store_ini_file
        fi
    ;;
   Personal)
        ln -sf $data_dir/personal-override $product_override_file
        if [ ! -f $app_store_ini_file ]; then
            ln -sf $app_store_ini_file_personal $app_store_ini_file
        fi
    ;;
esac

%files
%doc README.md
%license LICENSE
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/deepin-app-store/*
%{_datadir}/deepin-desktop-schemas/*
%{_datadir}/deepin-appstore/*

%changelog
* Wed Jul 21 2021 weidong <weidong@uniontech.com> - 5.8.0.26-2
- Using deepin-desktop-server instead of deepin-desktop-base

* Mon Jul 12 2021 weidong <weidong@uniontech.com> - 5.8.0.26-1
- Update 5.8.0.26

* Wed Aug 19 2020 chenbo pan <panchenbo@uniontech.com> - 5.5.0.6-2
- remove golang devel
* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.5.0.6-1
- Package init
