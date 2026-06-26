%define _prefix /gem_base/epics/support
%define name astlib
%define repository gemdev
%define debug_package %{nil}
%define arch %(uname -m)
%define checkout %(git log --pretty=format:'%h' -n 1)
%define git_hash %(git rev-parse --short HEAD 2>/dev/null || echo "nogit")

#These global defines are added to prevent stripping
# symbols on vxWorks cross-compiled code
# Getting 'strip' to work is probably only needed for
# building a related debug sub-package
#
# But this prevents all the strip warnings
# mrippa 20120202
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Summary: %{name} Package, a module for EPICS base
Name: %{name}
Version: 1.7.1
Release: 8.git.%{git_hash}%{?dist}
License: EPICS Open License
Group: Applications/Engineering
Source0: %{name}-%{version}.tar.gz
ExclusiveArch: %{arch}
Prefix: %{_prefix}
## You may specify dependencies here
BuildRequires: epics-base-devel = 7.0.7-0.git.f9e3717%{?dist}
BuildRequires: re2c
BuildRequires: gemini-ade
BuildRequires: timelib-devel = 2.1.4-3.git.a504360%{?dist}
BuildRequires: slalib-devel = 1.9.7-6.git.54d124d%{?dist}
## Switch dependency checking off
## AutoReqProv: no

%description
This is the module %{name}.

## If you want to have a devel-package to be generated uncomment the following:
%package devel
Summary: %{name}-devel Package
Group: Development/Gemini
Requires: %{name}
%description devel
This is the module %{name}.

%prep
%setup -q 

%build
make distclean uninstall
make

%install
export DONT_STRIP=1
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/%{name}
#cp -r bin $RPM_BUILD_ROOT/%{_prefix}/%{name}
cp -r lib $RPM_BUILD_ROOT/%{_prefix}/%{name}
cp -r include $RPM_BUILD_ROOT/%{_prefix}/%{name}
cp -r configure $RPM_BUILD_ROOT/%{_prefix}/%{name}
# find $RPM_BUILD_ROOT/%{_prefix}/%{name}/configure -name ".git" -exec rm -rf {} \;


%postun
if [ "$1" = "0" ]; then
	rm -rf %{_prefix}/%{name}
fi


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#   /%{_prefix}/%{name}/bin
   /%{_prefix}/%{name}/lib

%files devel
%defattr(-,root,root)
   /%{_prefix}/%{name}/include
   /%{_prefix}/%{name}/configure

%changelog
* Wed Jun 23 2021 Tiffany Shreves <tiffany.shreves@noirlab.edu> 1.7.1-8
- Fix tag number 

* Wed Jun 23 2021 Tiffany Shreves <tiffany.shreves@noirlab.edu> 1.7.1-6
- Remove worksupp path

* Wed Dec 30 2020 Roberto Rojas <rrojas@gemini.edu> 1.7.1-5
- removed dbd files

* Wed Dec 30 2020 Roberto Rojas <rrojas@gemini.edu> 1.7.1-4
- Added support modules required to the spec file

* Wed Dec 30 2020 Roberto Rojas <rrojas@gemini.edu> 1.7.1-3
- new package built with tito

* Wed Nov 18 2020 rrojas <rrojas@gemini.edu> 1.7.1
- copy based on astlib module
