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

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {
    'recipient': 'The Boss',
    'message': 'Mission Success'
  }
  json.dump(boss_message_dict, boss_message)