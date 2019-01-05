Name:                           meta-system
Version:                        1.0.0
Release:                        1%{?dist}
Summary:                        META-package for configure system
License:                        GPLv3

Source10:                       sysctl.custom.conf

%description
META-package for configure system.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%install
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/sysctl.d
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/00-sysctl.custom.conf

%files
%config(noreplace) %{_sysconfdir}/httpd/conf.d/00-sysctl.custom.conf

%changelog
* Wed Jan 02 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
