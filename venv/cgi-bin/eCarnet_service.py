#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import cgi as cgi_lib
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("Content-Type: application/xhtml+xml; charset = utf-8\n")

#Partie statique de la page HTML
print("""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<html xmlns="http://www.w3.org/1999/xhtml" lang="fr">
    <head>
    <title>eCarnet - Employés d'un service</title>
    </head>
    <body>
 """)
 
form = cgi_lib.FieldStorge()
service_id = str(form["service"].value)
db_connection = sqlite3.connect('myDB.db')
cd_connection.row_factory = sqlite3.Row
cursor = db_connection.cursor()
cursor.execute("SELECT name FROM Service WHERE id=" + service_id + ";")
row = cursor.fetchone()
service_name = str(row['name'])

print(' <h1>Employés du service " '+ service_name + '"</h1>')
cursor.execute("SELECT first_name, name, cellphone_number FROM Employee WHERE id_service=" + service_id + ";")
rows = cursor.fetchall()

print(' <ol>')
for row in rows:
    print(' <li>' + row['first_name'] + ', ' + row['name'] + ', ' + row['cellphone_number'] + '</li>')
print(""" </ol>
    </body>'
   </html>""")
db_connection.close()