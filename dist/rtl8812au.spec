Name:           rtl8812au
Version:        5.3.4
Release:        0
Summary:        RTL8812AU/21AU and RTL8814AU drivers.
Group:          Driverss/Network
License:        GPL
URL:            https://github.com/uniuuu/rtl8812au
Vendor:         Realtek www.realtek.com
Source0:    	%{name}-%{version}.tar.gz
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  git
BuildRequires:  perl >= 1:v5.10.1
BuildRequires:  perl(Module::Build) >= 0.35
BuildRequires:  perl(Test::Pod) >= 1.20
Requires:       git
Requires:       git-archive-all
Requires:       rpm-build
Requires:       perl(Getopt::Long)
Requires:       perl(List::Util)
Requires:       perl(IPC::System::Simple) >= 1.17
Requires:       perl(File::Temp)
Requires:       perl(Path::Class)
Requires:       perl(File::Path)
Requires:       perl(File::Copy)
Requires:       perl(File::Basename)
Requires:       perl(Pod::Usage)
BuildArch:	noarch
Packager: 	uniuuu

%description
Supports Realtek 8811, 8812, 8814 and 8821 chipsets
DKMS

This driver can be installed using [DKMS]. This is a system which will automatically recompile and install a kernel module when a new kernel gets installed or updated. To make use of DKMS, install the dkms package, which on Debian (based) systems is done like this:

%prep
%setup -q -n %{name}-%{version}

%build
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{gitman}/*
%{gitbin}/*

%changelog

