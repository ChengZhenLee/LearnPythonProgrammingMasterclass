# t = ("a", "b", "c")
# print(t)

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
        ("Bad Company", "Bad Company", 1974),
        ("Nightflight", "Budgie", 1981),
        ("More Mayhem", "Emilda May", 2011),
        ("Ride the Lightning", "Metallica", 1984),
        ]

print(len(albums))

# Unpack the tuple in the for statement
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))

# Unpack the tuple in the for block
for album in albums:
    name, artist, album = album[0], album[1], album[2]
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
# metallica[0] = "Master of Puppets"    tuples does not support item assignment

# turns the iterable (in this case a tuple) into a list
# metallica2 = list(metallica)
# print(metallica2)

# metallica2[0] = "Master of Puppets"
# print(metallica2)

# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)

# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])

# name, length, width, height, price = table
# print(length * width)