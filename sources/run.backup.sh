#!/usr/bin/env bash

# -------------------------------------------------------------------------------------------------------------------- #
# Backup databases.
# -------------------------------------------------------------------------------------------------------------------- #
# @author Kitsune Solar <kitsune.solar@gmail.com>
# @version 1.0.0
# -------------------------------------------------------------------------------------------------------------------- #

# -------------------------------------------------------------------------------------------------------------------- #
# Timestamp generator.
# -------------------------------------------------------------------------------------------------------------------- #

run.timestamp() {
    timestamp="$( date -u '+%Y-%m-%d.%T' )"

    echo ${timestamp}
}

# -------------------------------------------------------------------------------------------------------------------- #
# Backup databases.
# -------------------------------------------------------------------------------------------------------------------- #

db() {
    # Timestamp.
    timestamp="$( run.timestamp )"

    # DB user.
    db_user="${1}"

    # DB password.
    db_password="${2}"

    # DB host.
    db_host="${3}"

    # Mail.
    mail_to="${4}"

    # Path.
    path="${5}/${timestamp}"

    # Get mysql.
    mysql="$( which mysql )"

    # Get mysqldump.
    mysql_dump="$( which mysqldump )"

    # Get databases.
    databases=`${mysql} -u "${db_user}" -p"${db_password}" -h"${db_host}" -e "show databases;" | egrep -v "^(mysql|information_schema|performance_schema)$"`

    # Create backup directories.
    mkdir -p "${path}" && cd "${path}"

    # Backup databases.
    for database in ${databases}; do
        echo ""
        echo "--- Backup database: ${database} - ["

        ${mysql_dump}       \
        -u "${db_user}"     \
        -p"${db_password}"  \
        -h"${db_host}"      \
        --opt ${database} > "${database}.${timestamp}.sql" | gzip > "${database}.${timestamp}.sql.gz"

        echo "--- Backup database: ${database} - ]"
        echo ""
    done

    # Mail report.
    echo "$( ls -1hs )" | mailx -s "SRV: Backup Database" "${mail_to}"
}
