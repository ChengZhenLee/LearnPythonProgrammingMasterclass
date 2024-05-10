import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "newemail@update.com"
phone = input("Please enter the phone number ")

# This code is vulnerable to sql injection attacks
# update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
# Placeholders protects from sql injection attacks
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
print(update_sql)

update_cursor = db.cursor()

# executescript() will run multiple sql statements
# does not set the cursor row properly
update_cursor.executescript(update_sql)

# execute allows the use of placeholder tuples, in the case 
# the placeholders haven't been filled in the script with tuples
update_cursor.execute(update_sql, (new_email, phone))

print("{} row is updated".format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))
print()

# Commit at the cursor connection to db, instead of commiting entire db
# In case in later code, executions are performed which aren't
# meant to the committed
update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("*" * 20)

db.close() 