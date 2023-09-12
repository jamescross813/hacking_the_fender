import csv
import json

compromised_users = []

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for info in password_csv:
    password_row = info
    compromised_users.append(password_row['Username'])

with open('compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)