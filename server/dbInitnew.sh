#!/bin/bash
set -euo pipefail; # bash unofficial strict mode

DB_NAME="egordb"
DB_USER="egordb"
DB_PASS="$(openssl rand -hex 10)"

echo "CREATE DATABASE if not exists $DB_NAME;" | sudo mysql

echo "USE $DB_NAME if exists" | sudo mysql

echo "CREATE USER '$DB_USER'@'host' IDENTIFIED WITH authentication_plugin BY '$DB_PASS';" | sudo mysql



