Name:                           meta-system
Version:                        1.0.3
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
%{__mkdir} -p %{buildroot}/home/storage/cache
%{__mkdir} -p %{buildroot}/home/storage/databases
%{__mkdir} -p %{buildroot}/home/storage/databases/.backup
%{__mkdir} -p %{buildroot}/home/storage/databases/redis
%{__mkdir} -p %{buildroot}/home/storage/databases/mysql
%{__mkdir} -p %{buildroot}/home/storage/logs
%{__mkdir} -p %{buildroot}/home/storage/projects
%{__mkdir} -p %{buildroot}/home/storage/projects/.backup
%{__mkdir} -p %{buildroot}/home/storage/sessions
%{__mkdir} -p %{buildroot}/home/storage/tmp
%{__mkdir} -p %{buildroot}/home/storage/users

# Install configs.
%{__mkdir} -p %{buildroot}%{_sysconfdir}/sysctl.d
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/sysctl.d/00-sysctl.custom.conf

# Install scripts.
mkdir -p %{buildroot}%{_prefix}/local/bin

install -m 0755 %{SOURCE11} \
    %{buildroot}%{_prefix}/local/bin/run.backup.sh
install -m 0755 %{SOURCE12} \
    %{buildroot}%{_prefix}/local/bin/run.domain.sh

%files
%dir /home/storage/cache
%dir /home/storage/databases
%dir /home/storage/databases/.backup
%dir /home/storage/databases/redis
%dir /home/storage/databases/mysql
%dir /home/storage/logs
%dir /home/storage/projects
%dir /home/storage/projects/.backup
%dir /home/storage/sessions
%dir /home/storage/tmp
%dir /home/storage/users
%config(noreplace) %{_sysconfdir}/sysctl.d/00-sysctl.custom.conf
%{_prefix}/local/bin/run.backup.sh
%{_prefix}/local/bin/run.domain.sh

%changelog
* Fri Feb 15 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.3-1
- New version: 1.0.3.

* Thu Feb 14 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.2-1
- New version: 1.0.2.

* Tue Feb 12 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.1-1
- New version: 1.0.1.

* Wed Jan 02 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
