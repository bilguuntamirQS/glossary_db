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

with open('translations.csv') as file:
  reader = csv.reader(file)

  next(reader)
  for row in reader:
    cursor.execute("SELECT id FROM admin_users WHERE email = %s", (row[5], ))
    user = cursor.fetchone()
    if user is None:
      user = (1, )
    cursor.execute("SELECT id FROM words WHERE id = %s", (int(row[1]), ))
    word = cursor.fetchone()
    if word is not None:
      values.append((int(row[0]), int(row[1]), row[2], str(row[3]), int(row[4]), int(user[0]), row[6], row[6]))

sql = "INSERT INTO translations (id, word_id, translation, term, category_id, admin_user_id, created_at, updated_at) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"

cursor.executemany(sql, values)

db.commit()

print(cursor.rowcount, "was inserted")
