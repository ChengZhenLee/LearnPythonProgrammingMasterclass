import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', '6545678', 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', '1234', 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# fetches everything in the database and puts the cursor at the end
# print(cursor.fetchall())

# fetches one row
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("*" * 20)

cursor.close()
# commit so that the changes are saved into the database
db.commit()
db.close()
