import csv
from datetime import datetime
from db import Database

values = []

with open('users.csv') as file:
  reader = csv.reader(file)

  next(reader)
  for row in reader:
    values.append((row[0], row[1], row[2], '$2a$12$4c7SKvdcEhbBpeK25BE3ce4cdlLflNVnsGa8QT2nbiYQ52y7gQVjq', int(row[4]) - 1, row[5], row[5]))

import mysql.connector

db = mysql.connector.connect(
  host=Database.host,
  user=Database.user,
  password=Database.password,
  database=Database.database
)

cursor = db.cursor()

sql = "INSERT INTO admin_users ( email, name, lname, encrypted_password, permission, created_at, updated_at) VALUES ( %s, %s, %s, %s, %s, %s, %s)"

cursor.executemany(sql, values)

db.commit()

print(cursor.rowcount, "was inserted")