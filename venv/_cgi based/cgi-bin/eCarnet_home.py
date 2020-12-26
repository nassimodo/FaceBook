#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
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
    <title>eCarnet - Home</title>
    </head>
    <body>
    <h1>Bienvenue sur l'eCarnet</h1>
    <h2>Liste des amis</h2>
 """)
 
#Connexion à la base de données
db_connection = sqlite3.connect('myDB.db')
db_connection.row_factory = sqlite3.Row
cursor = db_connection.cursor()

#Sélection des enregistrements

cursor.execute("SELECT first_name, name, birth_date FROM Employee;")

#Création de la liste des employés
rows = cursor.fetchall()
print(' <ol>')
for row in rows:
    print(' <li>' + row['first_name'] + ' ' + row['name'] + ' ' + row['birth_date'] + '</li>')
print(' </ol>')

#Formulaire de recherche des ami d'une commune
print("""<h2>Amis par commune</h2>
<form action="eCarnet_service.py" method="get">
<p><select name="service">""")
cursor.execute("SELECT id, name FROM service ORDER BY name;")
rows = cursor.fetchall()
for row in rows:
    print(' <option value="' + str(row['id']) + '">' + row['name'] + '</option>')
print("""</select><input type="submit" value="Lister"/></p></form>""")
    


#Formulaire d'ajout d'un nouvel employé
print("""<h2>Ajouter un nouvel ami</h2>
    <form action="eCarnet_add_employee.py" method="get">
    <p>Prénom : <input type="text" name="first_name" /></p>
    <p>Nom :  <input type="text" name="name" /></p>
    <p>Anniversaire :  <input type="text" name="birth_date" /></p>
    <p>Email :  <input type="text" name="email" /></p>
    <p>Commune :  <select name="service">
""")

for row in rows:
    print(' <option value="' + str(row['id']) + '">' + row['name'] + '</option>')

print(""" </select></p>
    <p><input type="submit" value="Ajouter" /></p>
    </form>
    </body>
   </html>
   </meta>
""")

db_connection.close()