#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import cgi
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
    <title>eCarnet - Ajout d'un ami</title>
    </head>
    <body>
 """)
 
form = cgi.FieldStorage()
id_service = str(form["service"].value)
name = str(form["name"].value)
first_name = str(form["first_name"].value)
birth_date = str(form["birth_date"].value)
email = str(form["email"].value)
cellphone_number = "X"
home_phone_number = "X"


db_connection = sqlite3.connect('myDB.db')
db_connection.row_factory = sqlite3.Row
cursor = db_connection.cursor()

cursor.execute("SELECT MAX(registration_number) as max_id FROM Employee;")
max_registration_number = cursor.fetchone()[0]
registration_number = int(str(max_registration_number)) + 1
cursor.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?,?);", (registration_number, first_name, name, birth_date, email, home_phone_number, cellphone_number, id_service))
db_connection.commit()
db_connection.close()

print(' <h1>Ajout de l\'ami [' + first_name + ' ' + name + ']</h1>')
print(' <p>' + first_name + ' ' + name + ' a bien été ajouté dans la base de données.</p>')

print(""" <p><a href="eCarnet_home.py">Retour au eCarnet.</a></p>
    </body>
    </html>
    </meta>""")
 
 
 
