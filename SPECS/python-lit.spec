%global lit_version 15.0.7
#global rc_ver 1
#%%global post_ver 1

%bcond_without check

Name: python-lit
Version: %{lit_version}%{?rc_ver:~rc%{rc_ver}}
Release: 1%{?dist}
BuildArch: noarch

License: NCSA
Summary: Tool for executing llvm test suites
URL: https://pypi.python.org/pypi/lit
Source0: %{pypi_source lit %{lit_version}%{?rc_ver:rc%{rc_ver}}%{?post_ver:.post%{post_ver}}}

# for file check
%if %{with check}
BuildRequires: llvm-test
%endif
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
lit is a tool used by the LLVM project for executing its test suites.

%package -n python3-lit
Summary: LLVM lit test runner for Python 3

Requires: python3-setuptools

%description -n python3-lit
lit is a tool used by the LLVM project for executing its test suites.

%prep
%autosetup -n lit-%{lit_version}%{?rc_ver:rc%{rc_ver}}%{?post_ver:.post%{post_ver}} -p4

%build
%py3_build

%install
%py3_install

# Strip out #!/usr/bin/env python
sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python3_sitelib}/lit/*.py

%if %{with check}
%check
%{__python3} lit.py -v tests
%endif

%files -n python3-lit
%license LICENSE.TXT
%doc README.txt
%{python3_sitelib}/*
%{_bindir}/lit

%changelog
* Thu Jan 19 2023 Tom Stellard <tstellar@redhat.com> - 15.0.7-1
- Update to lit 15.0.7

* Tue Sep 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-1
- Update to lit 15.0.0

* Mon Jun 27 2022 Tom Stellard <tstellar@redhat.com> - 14.0.6-1
- Update to 14.0.6

* Thu Apr 07 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-1
- Update to 14.0.0

* Wed Feb 02 2022 Tom Stellard <tstellar@redhat.com> - 13.0.1-1
- 13.0.1 Release

* Fri Oct 15 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-1
- 13.0.0 Release

* Fri Jul 16 2021 sguelton@redhat.com - 12.0.1-1
- 12.0.1 release

* Thu May 6 2021 sguelton@redhat.com - 12.0.0-1
- 12.0.0 release

* Thu Oct 29 2020 sguelton@redhat.com - 0.11.0-1
- 0.11.0 final release

* Thu Sep 17 2020 sguelton@redhat.com - 0.11.0-0.1.rc1
- 0.11.0 rc1 Release

* Thu Apr 9 2020 sguelton@redhat.com - 0.10.0-1
- 0.10.0 final release

* Fri Sep 27 2019 Tom Stellard <tstellar@redhat.com> - 0.9.0-1
- 0.9.0 Release

* Wed Apr 17 2019 sguelton@redhat.com - 0.8.0-1
- 0.8.0 Release

* Fri Dec 14 2018 Tom Stellard <tstellar@redhat.com> - 0.7.1-1
- 0.7.1 Release

* Tue Nov 27 2018 Tom Stellard <tstellar@redhat.com> - 0.7.0-1
- 0.7.0 Release

* Fri Nov 16 2018 Lumír Balhar <lbalhar@redhat.com> - 0.6.0-6
- Require platform-python-setuptools instead of python3-setuptools
- Resolves: rhbz#1650540

* Mon Oct 01 2018 Tom Stellard <tstellar@redhat.com> - 0.6.0-5
- Drop SCL macros

* Wed Sep 12 2018 Tom Stellard <tstellar@redhat.com> - 0.6.0-4
- Use versioned python dependencies (python3)

* Mon Aug 27 2018 Tom Stellard <tstellar@redhat.com> - 0.6.0-3
- Fix python3 install

* Mon Aug 27 2018 Tom Stellard <tstellar@redhat.com> - 0.6.0-2
- Enable python3

* Tue Jul 10 2018 Tom Stellrad <tstellar@redhat.com> - 0.6.0-1
- 0.6.0 Release

* Mon Jul 02 2018 Tom Stellard <tstellar@redhat.com> - 0.5.1-4
- Drop python2

* Tue Jun 12 2018 Tom Stellard <tstellar@redhat.com> - 0.5.1-3
- Add BuildRequires: scl-utils-build

* Thu Jan 11 2018 Tom Stellard - 0.5.1-2
- Fix build on RHEL8

* Tue Jan 09 2018 Tom Stellard <tstellar@redhat.com> - 0.5.1-1
- Rebase to 0.5.1

* Thu Jun 08 2017 Tom Stellard <tstellar@redhat.com> - 0.5.0-7
- Build for llvm-toolset-7 rename

* Thu May 18 2017 Tom Stellard <tstellar@redhat.com> - 0.5.0-6
- Fix package names

* Wed May 10 2017 Tilmann Scheller <tschelle@redhat.com> - 0.5.0-5
- Next attempt to add runtime dependency on python-setuptools

* Tue May 09 2017 Tilmann Scheller <tschelle@redhat.com> - 0.5.0-4
- Properly add missing runtime dependency to python-setuptools

* Tue May 09 2017 Tilmann Scheller <tschelle@redhat.com> - 0.5.0-3
- Add missing runtime dependency to python-setuptools

* Fri Apr 28 2017 Tom Stellard <tstellar@redhat.com> - 0.5.0-2
- Add llvm-toolset-4 scl support

* Thu Mar 09 2017 Tom Stellard <tstellar@redhat.com> - 0.5.0-1
- Initial version
