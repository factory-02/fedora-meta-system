Name:                           meta-system
Version:                        1.0.1
Release:                        1%{?dist}
Summary:                        META-package for configure system
License:                        GPLv3

Source10:                       sysctl.custom.conf
Source11:                       run.backup.sh
Source12:                       run.domain.sh

%description
META-package for configure system.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%install
# Create directories.
install -p -d -m 0755 %{buildroot}/home/storage/cache
install -p -d -m 0755 %{buildroot}/home/storage/databases
install -p -d -m 0755 %{buildroot}/home/storage/databases/.backup
install -p -d -m 0755 %{buildroot}/home/storage/databases/redis
install -p -d -m 0755 %{buildroot}/home/storage/databases/mysql
install -p -d -m 0755 %{buildroot}/home/storage/logs
install -p -d -m 0755 %{buildroot}/home/storage/projects
install -p -d -m 0755 %{buildroot}/home/storage/projects/.backup
install -p -d -m 0755 %{buildroot}/home/storage/sessions
install -p -d -m 0755 %{buildroot}/home/storage/tmp
install -p -d -m 0755 %{buildroot}/home/storage/users

# Install configs.
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/sysctl.d
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/sysctl.d/00-sysctl.custom.conf

# Install scripts.
install -p -m 0755 %{SOURCE11} \
    %{buildroot}%{_prefix}/bin/run.backup.sh
install -p -m 0755 %{SOURCE12} \
    %{buildroot}%{_prefix}/bin/run.domain.sh

%files
%dir %{_sysconfdir}/nginx/vhosts.d
%config(noreplace) %{_sysconfdir}/sysctl.d/00-sysctl.custom.conf
%{_prefix}/bin/run.backup.sh
%{_prefix}/bin/run.domain.sh

%changelog
* Tue Feb 12 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.1-1
- New version: 1.0.1.

* Wed Jan 02 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
