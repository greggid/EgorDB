#!/bin/bash

set -euo pipefail; # bash unofficial strict mode

DB_NAME="egordb"
DB_USER="egordb"
DB_PASS="$(openssl rand -hex 10)"

echo "CREATE DATABASE if not exists $DB_NAME;" | sudo mysql

echo "USE $DB_NAME if exists" | sudo mysql

echo "CREATE USER if not exists '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASS';" | sudo mysql

echo "ALTER USER '$DB_USER'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';" | sudo mysql

# echo "GRANT PRIVILEGE ON '$DB_NAME' TO '$DB_USER'@'localhost';" | sudo mysql

echo "Password: ";


