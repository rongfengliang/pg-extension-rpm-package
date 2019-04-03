Name:           nvl-pg-extension
Version:        1.0
Release:        1%{?dist}
Summary:        this is a postgresql extension nvl function just like oracle
License:        APACHE
URL:            https://github.com/rongfengliang/postgres-extension-demo
Source:         https://github.com/rongfengliang/nvl-pg-extension/archive/v1.0.zip

%prep
%setup -q

%description
this is a postgresql extension nvl function just like oracle

%install
%{make_install} PREFIX=%{_prefix}

%files
/usr/pgsql-10/share/extension/nvlfunc--1.0.sql
/usr/pgsql-10/share/extension/nvlfunc.control