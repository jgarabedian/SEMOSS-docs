import sqlite3
import csv
import os
from app import APP_DIR

EXPORT_DIR = os.path.join(APP_DIR, 'export.csv')

with open(EXPORT_DIR, 'w+') as write_file:
    conn = sqlite3.connect(os.path.join(APP_DIR, 'docs.db'))
    c = conn.cursor()
    print(c.fetchall())

# with sqlite3.connect(DATABASE) as connection:
#     csvWriter = csv.writer(open("output.csv", "w"))
#     c = connection.cursor()
#
#     rows = c.fetchall()
#     for i in rows:
#         csvWriter.writerow(i)


