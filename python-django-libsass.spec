%global pypi_name django-libsass
%global desc %{expand: \
A django-compressor filter to compile Sass files using libsass.}

%bcond tests 1

Name:           python-%{pypi_name}
Version:        0.9
Release:        %autorelease
Summary:        A django-compressor filter to compile Sass files using libsass

License:        BSD
URL:            https://github.com/torchbox/django-libsass
Source0:        %pypi_source

BuildArch:      noarch

%description %{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files django_libsass

%if %{with tests}
%check
# NOTE: we do not use %tox macro as there is no default tox env based on python version
# in upstream tox.ini file. Currently, the only test dependency is Django and it's installed
# by pyproject_buildrequires macro as a transitive dependency of django-compressor.
# we run the runtest.py python script.
%{__python3} runtests.py
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
