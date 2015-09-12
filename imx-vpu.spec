%define	major	4
%define	libname	%mklibname vpu %{major}
%define	devname	%mklibname -d vpu

Summary:	Freescale VPU library
Name:		imx-vpu
Version:	5.4.28
Release:	2
License:	Proprietary
Group:		System/Libraries
# downloaded and repackaged from:
# http://www.freescale.com/lgfiles/NMG/MAD/YOCTO/imx-vpu-3.10.17-1.0.0.bin
URL:		http://www.freescale.com
Source0:	%{name}-%{version}.tar.xz
Patch0:		imx-vpu-lib-1.0.0-cflags.patch
ExclusiveArch:	armv7hl armv7hnl

%description
Freescale VPU library.

%package -n	%{libname}
Summary:	Freescale VPU library
Group:		System/Libraries

%description -n	%{libname}
Freescale VPU library.

%package -n	%{devname}
Summary:	Development files for Freescale VPU library
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
Development files for Freescale VPU library.

%prep
%setup -q
%apply_patches

%build
%setup_compile_flags
%make LDFLAGS="%{ldflags} -Wl,--build-id" PLATFORM=IMX6Q

%install
%makeinstall_std PLATFORM=IMX6Q DEST_DIR=%{buildroot}

%files -n %{libname}
%{_libdir}/libvpu.so.%{major}*

%files -n %{devname}
%{_libdir}/libvpu.so
%{_libdir}/libvpu.a
%{_includedir}/vpu_io.h
%{_includedir}/vpu_lib.h
