#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v24
# autospec commit: a88ffdc
#
%define keepstatic 1
Name     : libcap
Version  : 2.76
Release  : 72
URL      : https://mirrors.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-2.76.tar.gz
Source0  : https://mirrors.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-2.76.tar.gz
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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


%package staticdev
Summary: staticdev components for the libcap package.
Group: Default
Requires: libcap-dev = %{version}-%{release}

%description staticdev
staticdev components for the libcap package.


%package staticdev32
Summary: staticdev32 components for the libcap package.
Group: Default
Requires: libcap-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the libcap package.


%prep
%setup -q -n libcap-2.76
cd %{_builddir}/libcap-2.76
pushd ..
cp -a libcap-2.76 build32
popd
pushd ..
cp -a libcap-2.76 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744639948
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}  LIBATTR=yes PAM_CAP=yes INDENT= SYSTEM_HEADERS=/usr/include RAISE_SETFCAP=no

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
make  %{?_smp_mflags}  LIBATTR=yes PAM_CAP=yes INDENT= SYSTEM_HEADERS=/usr/include RAISE_SETFCAP=no lib=/usr/lib32 LIBATTR=yes PAM_CAP=yes INDENT= SYSTEM_HEADERS=/usr/include RAISE_SETFCAP=no
popd
pushd ../buildavx2
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}  LIBATTR=yes PAM_CAP=yes INDENT= SYSTEM_HEADERS=/usr/include RAISE_SETFCAP=no
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1744639948
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libcap
cp %{_builddir}/libcap-%{version}/License %{buildroot}/usr/share/package-licenses/libcap/682fe08e594eabefd7970be40b1908df3d7f5c46 || :
cp %{_builddir}/libcap-%{version}/cap/License %{buildroot}/usr/share/package-licenses/libcap/2744365535d0c90f5b952236cd72ef1755d0440e || :
cp %{_builddir}/libcap-%{version}/pam_cap/License %{buildroot}/usr/share/package-licenses/libcap/228cae5d7ba8881444454a276eaf88f31eb27978 || :
cp %{_builddir}/libcap-%{version}/psx/License %{buildroot}/usr/share/package-licenses/libcap/e898bee369adf3e2b7505ecad40c1b43e50bce9a || :
export GOAMD64=v2
pushd ../build32/
%make_install32 DESTDIR=%{buildroot} prefix=/usr SBINDIR=/usr/bin RAISE_SETFCAP=no DESTDIR=%{buildroot} LIBDIR=/usr/lib32 prefix=/usr SBINDIR=/usr/bin RAISE_SETFCAP=no PAM_CAP=no
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3 DESTDIR=%{buildroot} prefix=/usr SBINDIR=/usr/bin RAISE_SETFCAP=no
popd
GOAMD64=v2
%make_install DESTDIR=%{buildroot} prefix=/usr SBINDIR=/usr/bin RAISE_SETFCAP=no
## install_append content
mkdir -p %{buildroot}/usr/lib32/pkgconfig
sed 's/64/32/g' %{buildroot}/usr/lib64/pkgconfig/libcap.pc > %{buildroot}/usr/lib32/pkgconfig/libcap.pc
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/include/sys/psx_syscall.h
/usr/lib64/libcap.so
/usr/lib64/libpsx.so
/usr/lib64/pkgconfig/libcap.pc
/usr/lib64/pkgconfig/libpsx.pc
/usr/share/man/man3/__psx_syscall.3
/usr/share/man/man3/cap_clear.3
/usr/share/man/man3/cap_clear_flag.3
/usr/share/man/man3/cap_compare.3
/usr/share/man/man3/cap_copy_ext.3
/usr/share/man/man3/cap_copy_int.3
/usr/share/man/man3/cap_copy_int_check.3
/usr/share/man/man3/cap_drop_bound.3
/usr/share/man/man3/cap_dup.3
/usr/share/man/man3/cap_fill.3
/usr/share/man/man3/cap_fill_flag.3
/usr/share/man/man3/cap_free.3
/usr/share/man/man3/cap_from_name.3
/usr/share/man/man3/cap_from_text.3
/usr/share/man/man3/cap_func_launcher.3
/usr/share/man/man3/cap_get_bound.3
/usr/share/man/man3/cap_get_fd.3
/usr/share/man/man3/cap_get_file.3
/usr/share/man/man3/cap_get_flag.3
/usr/share/man/man3/cap_get_mode.3
/usr/share/man/man3/cap_get_nsowner.3
/usr/share/man/man3/cap_get_pid.3
/usr/share/man/man3/cap_get_proc.3
/usr/share/man/man3/cap_get_secbits.3
/usr/share/man/man3/cap_iab.3
/usr/share/man/man3/cap_iab_compare.3
/usr/share/man/man3/cap_iab_dup.3
/usr/share/man/man3/cap_iab_fill.3
/usr/share/man/man3/cap_iab_from_text.3
/usr/share/man/man3/cap_iab_get_pid.3
/usr/share/man/man3/cap_iab_get_proc.3
/usr/share/man/man3/cap_iab_get_vector.3
/usr/share/man/man3/cap_iab_init.3
/usr/share/man/man3/cap_iab_set_proc.3
/usr/share/man/man3/cap_iab_set_vector.3
/usr/share/man/man3/cap_iab_to_text.3
/usr/share/man/man3/cap_init.3
/usr/share/man/man3/cap_launch.3
/usr/share/man/man3/cap_launcher_callback.3
/usr/share/man/man3/cap_launcher_set_chroot.3
/usr/share/man/man3/cap_launcher_set_iab.3
/usr/share/man/man3/cap_launcher_set_mode.3
/usr/share/man/man3/cap_launcher_setgroups.3
/usr/share/man/man3/cap_launcher_setuid.3
/usr/share/man/man3/cap_max_bits.3
/usr/share/man/man3/cap_mode.3
/usr/share/man/man3/cap_mode_name.3
/usr/share/man/man3/cap_new_launcher.3
/usr/share/man/man3/cap_prctl.3
/usr/share/man/man3/cap_prctlw.3
/usr/share/man/man3/cap_proc_root.3
/usr/share/man/man3/cap_set_fd.3
/usr/share/man/man3/cap_set_file.3
/usr/share/man/man3/cap_set_flag.3
/usr/share/man/man3/cap_set_mode.3
/usr/share/man/man3/cap_set_nsowner.3
/usr/share/man/man3/cap_set_proc.3
/usr/share/man/man3/cap_set_secbits.3
/usr/share/man/man3/cap_set_syscall.3
/usr/share/man/man3/cap_setgroups.3
/usr/share/man/man3/cap_setuid.3
/usr/share/man/man3/cap_size.3
/usr/share/man/man3/cap_to_name.3
/usr/share/man/man3/cap_to_text.3
/usr/share/man/man3/capgetp.3
/usr/share/man/man3/capsetp.3
/usr/share/man/man3/libcap.3
/usr/share/man/man3/libpsx.3
/usr/share/man/man3/psx_load_syscalls.3
/usr/share/man/man3/psx_set_sensitivity.3
/usr/share/man/man3/psx_syscall.3
/usr/share/man/man3/psx_syscall3.3
/usr/share/man/man3/psx_syscall6.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcap.so
/usr/lib32/libpsx.so
/usr/lib32/pkgconfig/32libcap.pc
/usr/lib32/pkgconfig/32libpsx.pc
/usr/lib32/pkgconfig/libcap.pc
/usr/lib32/pkgconfig/libpsx.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcap.so.2
/usr/lib64/libcap.so.2.76
/usr/lib64/libpsx.so.2
/usr/lib64/libpsx.so.2.76
/usr/lib64/security/pam_cap.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libcap.so.2
/usr/lib32/libcap.so.2.76
/usr/lib32/libpsx.so.2
/usr/lib32/libpsx.so.2.76

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libcap/228cae5d7ba8881444454a276eaf88f31eb27978
/usr/share/package-licenses/libcap/2744365535d0c90f5b952236cd72ef1755d0440e
/usr/share/package-licenses/libcap/682fe08e594eabefd7970be40b1908df3d7f5c46
/usr/share/package-licenses/libcap/e898bee369adf3e2b7505ecad40c1b43e50bce9a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/capsh.1
/usr/share/man/man5/capability.conf.5
/usr/share/man/man7/cap_text_formats.7
/usr/share/man/man8/captree.8
/usr/share/man/man8/getcap.8
/usr/share/man/man8/getpcaps.8
/usr/share/man/man8/pam_cap.8
/usr/share/man/man8/setcap.8

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libcap.a
/usr/lib64/libpsx.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libcap.a
/usr/lib32/libpsx.a
