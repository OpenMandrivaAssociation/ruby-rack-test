%define oname rack-test

Name:       ruby-%{oname}
Version:    0.6.2
Release:    2
Summary:    Simple testing API built on Rack
Group:      Development/Ruby
License:    MIT
URL:        https://github.com/brynary/rack-test
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRequires: ruby-RubyGems
BuildArch:  noarch
%rename     rubygem-%{oname}

%description
Rack::Test is a small, simple testing API for Rack apps. It can be used on its
own or as a reusable starting point for Web frameworks and testing libraries
to build on. Most of its initial functionality is an extraction of Merb 1.0's
request helpers feature.

%prep

%build

%install
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gitignore
rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
