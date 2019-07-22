#!/usr/bin/env bash

echo  "CREATE DATABASE IF NOT EXISTS ${1} CHARACTER SET utf8 COLLATE utf8_general_ci;" > /docker-entrypoint-initdb.d/init.sql;
/usr/local/bin/docker-entrypoint.sh --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --max-allowed-packet=268435456
