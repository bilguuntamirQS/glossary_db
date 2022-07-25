import csv
from datetime import datetime

import mysql.connector

db = mysql.connector.connect(
  host=Database.host,
  user=Database.user,
  password=Database.password,
  database=Database.database
)

cursor = db.cursor()

values = []

with open('words.csv') as file:
  reader = csv.reader(file)

  next(reader)
  for row in reader:
    cursor.execute("SELECT * FROM admin_users WHERE email = %s", (row[3], ))
    user = cursor.fetchone()
    values.append((int(row[0]), row[1], row[2], row[2], int(user[0])))


sql = "INSERT INTO words ( id, word_text, created_at, updated_at, admin_user_id) VALUES ( %s, %s, %s, %s, %s)"

cursor.executemany(sql, values)

db.commit()

print(cursor.rowcount, "was inserted")