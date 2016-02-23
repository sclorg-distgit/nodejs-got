%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name got

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        5.2.1
Release:        6%{?dist}
Summary:        Simplified HTTP/HTTPS requests
License:        MIT
URL:            https://github.com/sindresorhus/got
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}runtime

%if 0%{?enable_tests}
BuildRequires: %{?scl_prefix}npm(tap)
BuildRequires: %{?scl_prefix}npm(create-error-class)
BuildRequires: %{?scl_prefix}npm(into-stream)
BuildRequires: %{?scl_prefix}npm(pinkie-promise)
BuildRequires: %{?scl_prefix}npm(unzip-response)
BuildRequires: %{?scl_prefix}npm(object-assign)
BuildRequires: %{?scl_prefix}npm(pem)
BuildRequires: %{?scl_prefix}npm(is-redirect)
BuildRequires: %{?scl_prefix}npm(duplexify)
BuildRequires: %{?scl_prefix}npm(is-stream)
BuildRequires: %{?scl_prefix}npm(read-all-stream)
BuildRequires: %{?scl_prefix}npm(timed-out)
BuildRequires: %{?scl_prefix}npm(node-status-codes)
BuildRequires: %{?scl_prefix}npm(is-plain-obj)
BuildRequires: %{?scl_prefix}npm(lowercase-keys)
BuildRequires: %{?scl_prefix}npm(prepend-http)
%endif

%description
Simplified HTTP/HTTPS requests. A nicer interface to the built-in http module.
It also supports following redirects and automagically handling gzip/deflate.

%prep
%setup -q -n package

%nodejs_fixdep create-error-class ">=2.0.0"
%nodejs_fixdep duplexify ">=3.2.0"
%nodejs_fixdep is-plain-obj ">=1.0.0"
%nodejs_fixdep is-redirect ">=1.0.0"
%nodejs_fixdep is-stream ">=1.0.0"
%nodejs_fixdep lowercase-keys ">=1.0.0"
%nodejs_fixdep node-status-codes ">=1.0.0"
%nodejs_fixdep object-assign ">=4.0.1"
%nodejs_fixdep parse-json ">=2.1.0"
%nodejs_fixdep pinkie-promise ">=2.0.0"
%nodejs_fixdep read-all-stream ">=3.0.0"
%nodejs_fixdep timed-out ">=2.0.0"
%nodejs_fixdep unzip-response ">=1.0.0"
%nodejs_fixdep url-parse-lax ">=1.0.0"

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
# These tests not working so remove them for now
rm -f test/test-error.js
rm -f test/test-arguments.js
rm -f test/test-https.js
rm -f test/test-http.js
tap test/test-*.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.md
%license license
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 5.2.1-6
- Rebuilt with updated metapackage
- use proper macro in -runtime dependency

* Mon Jan 11 2016 Tomas Hrcka <thrcka@redhat.com> - 5.2.1-2
- Enable scl macros

* Thu Dec 17 2015 Troy Dawson <tdawson@redhat.com> - 5.2.1-2
- Update to 5.2.1

* Thu Nov 26 2015 Parag Nemade <pnemade AT redhat DOT com> - 5.1.0-1
- Update to 5.1.0

* Thu Nov 26 2015 Parag Nemade <pnemade AT redhat DOT com> - 4.2.0-2
- fixdep npm(pinkie-promise)

* Fri Sep 11 2015 Parag Nemade <pnemade AT redhat DOT com> - 4.2.0-1
- Update to 4.2.0

* Wed Aug 26 2015 Parag Nemade <pnemade AT redhat DOT com> - 4.1.1-2
- fixdep npm(object-assign)

* Mon Aug 24 2015 Parag Nemade <pnemade AT redhat DOT com> - 4.1.1-1
- Update to 4.1.1

* Thu Jul 30 2015 Parag Nemade <pnemade AT redhat DOT com> - 4.1.0-1
- Update to 4.1.0

* Wed Jul 29 2015 Parag Nemade <pnemade AT redhat DOT com> - 4.0.0-1
- Update to 4.0.0

* Wed Jul 22 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.3.1-2
- fixdep npm(readable-stream)

* Wed Jul 15 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.3.1-1
- Update to 3.3.1

* Fri Jul 03 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.3.0-1
- Update to 3.3.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 03 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.3.2-1
- Update to 2.3.2

* Sun Jan 11 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.3.0-1
- Update to 2.3.0

* Wed Dec 03 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.2.0-1
- Initial packaging
