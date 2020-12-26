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
    <title>eCarnet - Amis de la commune</title>
    </head>
    <body>
 """)
 
form = cgi_lib.FieldStorage()
service_id = str(form["service"].value)
db_connection = sqlite3.connect('myDB.db')
db_connection.row_factory = sqlite3.Row
cursor = db_connection.cursor()
cursor.execute("SELECT name FROM Service WHERE id=" + service_id + ";")
row = cursor.fetchone()
service_name = str(row['name'])
cursor.execute("SELECT location FROM Service WHERE id=" + service_id + ";")
row = cursor.fetchone()
service_location = str(row['location'])

print(' <h1>Amis de la commune ['+ service_name + '-' + service_location + ']</h1>')
cursor.execute("SELECT first_name, name, cellphone_number FROM Employee WHERE id_service=" + service_id + ";")
rows = cursor.fetchall()

print(' <ol>')
for row in rows:
    print(' <li>' + row['first_name'] + ', ' + row['name'] + ', ' + row['cellphone_number'] + '</li>')
print(""" </ol> <p><a href="eCarnet_home.py">Retour au eCarnet.</a></p>
    </body>'
   </html>
   </meta>""")
db_connection.close()