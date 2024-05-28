text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]

print(capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

lc_words = text.split(' ')
print(lc_words)

lc_words = [word for word in text.split(' ')]
print(lc_words)

# NOTE: when a list comprehension doesn't have brackets
# eg. words = word.upper() for word in text.split(' ')
# This is then not a list comprehension, but a generator expression