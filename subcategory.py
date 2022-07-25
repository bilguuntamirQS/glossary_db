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

with open('subareas.csv') as file:
  reader = csv.reader(file)

  next(reader)
  for row in reader:
    if row[3] is 'NULL':
      row[3] = None
    values.append((int(row[0]) + 7, row[1], row[2], row[3], row[4], row[4]))


sql = "INSERT INTO categories (id, parent_id, category_name_en, category_name_mn, created_at, updated_at) VALUES ( %s, %s, %s, %s, %s, %s)"

cursor.executemany(sql, values)

db.commit()

print(cursor.rowcount, "was inserted")