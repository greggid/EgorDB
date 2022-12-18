#!bin/bash

DB_NAME="egordb"
DB_USER="egordb"
DB_PASS="$(openssl rand -hex 10)"


echo "create database $DB_NAME;" | sudo mysql

echo "grant all privileges on $DB_NAME.* TO '$DB_USER'@'localhost' identified by '$DB_PASS;" 
