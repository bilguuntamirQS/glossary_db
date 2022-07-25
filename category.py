import csv
from datetime import datetime
from db import Database

import mysql.connector

db = mysql.connector.connect(
  host=Database.host,
  user=Database.user,
  password=Database.password,
  database=Database.database
)

cursor = db.cursor()

values = []

with open('areas.csv') as file:
  reader = csv.reader(file)

  next(reader)
  for row in reader:
    if row[2] == 'NULL':
      row[2] = None
    values.append((row[1], row[2], row[3], row[3], 1))


sql = "INSERT INTO categories ( category_name_en, category_name_mn, created_at, updated_at, level) VALUES ( %s, %s, %s, %s, %s)"

cursor.executemany(sql, values)

db.commit()

print(cursor.rowcount, "was inserted")