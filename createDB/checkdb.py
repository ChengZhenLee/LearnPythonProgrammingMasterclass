import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Please enter a name ")

# for row in conn.execute("SELECT * FROM contacts WHERE name = ?",(name,)):
# A tuple needs to be passed to the method for use of placeholder
# Commas are needed within the parantheses to be considered a tuple
for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)

conn.close()