#!/bin/bash

# if you change the schema do this (?)

rm database.db 
sqlite3 database.db < schema.sql