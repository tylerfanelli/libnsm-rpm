%bcond check 1
%global debug_package %{nil}

Name:           libnsm
Version:        0.4.0
Release:        %{autorelease}
Summary:        C library for Nitro Secure Module (NSM)

License:        Apache-2.0
URL:            https://github.com/aws/aws-nitro-enclaves-nsm-api
Source0:        v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  glibc-devel
BuildRequires:  cargo-rpm-macros

BuildRequires:  (crate(libc/default) >= 0.2.0 with crate(libc/default) < 0.3.0~)

%global _description %{expand:
C library for Nitro Secure Module (NSM).}

%description %{_description}

%package devel
Summary: Header files and libraries for libnsm development
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The libnsm-devel package containes the libraries and headers needed to
develop programs that use the libnsm Nitro Secure Module (NSM) C library.

%prep
%autosetup -n aws-nitro-enclaves-nsm-api-%{version}
%{cargo_prep}

%generate_buildrequires
%cargo_generate_buildrequires

%build
%{cargo_build} --package nsm-lib

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} INCLUDEDIR=%{_includedir}

%files
%license LICENSE
%{_includedir}/nsm.h
%{_libdir}/pkgconfig/libnsm.pc
%{_libdir}/libnsm.so
%{_libdir}/libnsm.a

%changelog
* Wed Feb 25 2026 Tyler Fanelli <tfanelli@redhat.com> - 0.1.0-1
- Initial version for Fedora review.
