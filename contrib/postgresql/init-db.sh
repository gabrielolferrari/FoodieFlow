#!/bin/bash

cd /docker-entrypoint-initdb.d

psql -U postgres -c "CREATE DATABASE \"FIAP\";"
psql -U postgres --dbname "FIAP" -f migrate.sql