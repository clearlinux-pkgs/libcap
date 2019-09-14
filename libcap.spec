#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libcap
Version  : 2.27
Release  : 34
URL      : https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-2.27.tar.xz
Source0  : https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-2.27.tar.xz
Summary  : capability library: includes libcap2 file caps, setcap, getcap and capsh
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: libcap-bin = %{version}-%{release}
Requires: libcap-lib = %{version}-%{release}
Requires: libcap-license = %{version}-%{release}
Requires: libcap-man = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : Linux-PAM-dev32
BuildRequires : attr-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : grep
BuildRequires : ldd
Patch1: 0001-Fix-misc-build-issues.patch

%description
This is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.

%package bin
Summary: bin components for the libcap package.
Group: Binaries
Requires: libcap-license = %{version}-%{release}

%description bin
bin components for the libcap package.


%package dev
Summary: dev components for the libcap package.
Group: Development
Requires: libcap-lib = %{version}-%{release}
Requires: libcap-bin = %{version}-%{release}
Provides: libcap-devel = %{version}-%{release}
Requires: libcap = %{version}-%{release}

%description dev
dev components for the libcap package.


%package dev32
Summary: dev32 components for the libcap package.
Group: Default
Requires: libcap-lib32 = %{version}-%{release}
Requires: libcap-bin = %{version}-%{release}
Requires: libcap-dev = %{version}-%{release}

%description dev32
dev32 components for the libcap package.


%package lib
Summary: lib components for the libcap package.
Group: Libraries
Requires: libcap-license = %{version}-%{release}

%description lib
lib components for the libcap package.


%package lib32
Summary: lib32 components for the libcap package.
Group: Default
Requires: libcap-license = %{version}-%{release}

%description lib32
lib32 components for the libcap package.


%package license
Summary: license components for the libcap package.
Group: Default

%description license
license components for the libcap package.


%package man
Summary: man components for the libcap package.
Group: Default

%description man
man components for the libcap package.


%prep
%setup -q -n libcap-2.27
%patch1 -p1
pushd ..
cp -a libcap-2.27 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568144112
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags} lib=/usr/lib64 LIBATTR=yes PAM_CAP=yes INDENT= SYSTEM_HEADERS=/usr/include RAISE_SETFCAP=no

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
make  %{?_smp_mflags} lib=/usr/lib64 LIBATTR=yes PAM_CAP=yes INDENT= SYSTEM_HEADERS=/usr/include RAISE_SETFCAP=nolib=/usr/lib32 LIBATTR=yes PAM_CAP=yes INDENT= SYSTEM_HEADERS=/usr/include RAISE_SETFCAP=no
popd

%install
export SOURCE_DATE_EPOCH=1568144112
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libcap
cp License %{buildroot}/usr/share/package-licenses/libcap/License
cp pam_cap/License %{buildroot}/usr/share/package-licenses/libcap/pam_cap_License
pushd ../build32/
%make_install32 DESTDIR=%{buildroot} LIBDIR=/usr/lib64 prefix=/usr SBINDIR=/usr/bin RAISE_SETFCAP=no DESTDIR=%{buildroot} LIBDIR=/usr/lib32 prefix=/usr SBINDIR=/usr/bin RAISE_SETFCAP=no PAM_CAP=no
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install DESTDIR=%{buildroot} LIBDIR=/usr/lib64 prefix=/usr SBINDIR=/usr/bin RAISE_SETFCAP=no

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/capsh
/usr/bin/getcap
/usr/bin/getpcaps
/usr/bin/setcap

%files dev
%defattr(-,root,root,-)
/usr/include/sys/capability.h
/usr/lib64/libcap.so
/usr/lib64/pkgconfig/libcap.pc
/usr/share/man/man3/cap_clear.3
/usr/share/man/man3/cap_clear_flag.3
/usr/share/man/man3/cap_compare.3
/usr/share/man/man3/cap_copy_ext.3
/usr/share/man/man3/cap_copy_int.3
/usr/share/man/man3/cap_drop_bound.3
/usr/share/man/man3/cap_dup.3
/usr/share/man/man3/cap_free.3
/usr/share/man/man3/cap_from_name.3
/usr/share/man/man3/cap_from_text.3
/usr/share/man/man3/cap_get_bound.3
/usr/share/man/man3/cap_get_fd.3
/usr/share/man/man3/cap_get_file.3
/usr/share/man/man3/cap_get_flag.3
/usr/share/man/man3/cap_get_pid.3
/usr/share/man/man3/cap_get_proc.3
/usr/share/man/man3/cap_init.3
/usr/share/man/man3/cap_set_fd.3
/usr/share/man/man3/cap_set_file.3
/usr/share/man/man3/cap_set_flag.3
/usr/share/man/man3/cap_set_proc.3
/usr/share/man/man3/cap_size.3
/usr/share/man/man3/cap_to_name.3
/usr/share/man/man3/cap_to_text.3
/usr/share/man/man3/capgetp.3
/usr/share/man/man3/capsetp.3
/usr/share/man/man3/libcap.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcap.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcap.so.2
/usr/lib64/libcap.so.2.27
/usr/lib64/security/pam_cap.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libcap.so.2
/usr/lib32/libcap.so.2.27

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libcap/License
/usr/share/package-licenses/libcap/pam_cap_License

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/capsh.1
/usr/share/man/man8/getcap.8
/usr/share/man/man8/setcap.8
