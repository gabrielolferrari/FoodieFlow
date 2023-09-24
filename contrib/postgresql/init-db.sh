#!/bin/bash

cd /docker-entrypoint-initdb.d

psql -U postgres -c "CREATE DATABASE \"FIAP_postgresql\";"
psql -U postgres --dbname "FIAP_postgresql" -f migrate.sql