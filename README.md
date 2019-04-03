# demo pg extension with rpm pacakge

## how to running

* install rpm tools

> for centos os

```code
yum install  -y rpm-build rpmdevtools

```

* init setuptree

> with rpmdev-setuptree

```code
rpmdev-setuptree
```

* copy  specs file for package

```code

copy  nvl-pg-extension.spec to ~/rpmbuild/SPECS
```

* download source code

```code
spectool -g -R ~/rpmbuild/SPECS/nvl-pg-extension.spec

```

* build rpm pacakge

```code
rpmbuild -bb ~/rpmbuild/SPECS/nvl-pg-extension.spec

```