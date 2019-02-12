Name:                           meta-system
Version:                        1.0.1
Release:                        1%{?dist}
Summary:                        META-package for configure system
License:                        GPLv3

Source10:                       sysctl.custom.conf
Source11:                       run.backup.db.sh
Source12:                       run.domain.install.sh

%description
META-package for configure system.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%install
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/sysctl.d
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/sysctl.d/00-sysctl.custom.conf

install -p -m 0755 %{SOURCE11} \
    %{buildroot}%{_prefix}/local/bin/run.backup.sh
install -p -m 0755 %{SOURCE12} \
    %{buildroot}%{_prefix}/local/bin/run.domain.sh

%files
%config(noreplace) %{_sysconfdir}/sysctl.d/00-sysctl.custom.conf
%{_prefix}/local/bin/run.backup.sh
%{_prefix}/local/bin/run.domain.sh

%changelog
* Tue Feb 12 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.1-1
- New version: 1.0.1.

* Wed Jan 02 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
