import timeit
text = "what have the romans ever done for us"

def text_comp():
    capitals = [char.upper() for char in text]
    # print(capitals)
    return capitals

# use map
# Applies str.upper to text and creates an iterable
def text_map():
    map_capitals = list(map(str.upper, text))
    # print(map_capitals)
    return map_capitals

def words_comp():
    words = [word.upper() for word in text.split(' ')]
    # print(words)
    return words

# use map
def words_map():
    map_words = list(map(str.upper, text.split(' ')))
    # print(map_words)
    return map_words

for x in map(str.upper, text.split(' ')):
    print(x)

if __name__ == "__main__":
    print(text_comp())
    print(text_map())
    print(words_comp())
    print(words_map())

    # Call the function in timeit
    # print(timeit.timeit("text_comp()", setup="from __main__ import text_comp", number=10000))
    # print(timeit.timeit("text_map()", setup="from __main__ import text_map", number=10000))
    # print(timeit.timeit("words_comp()", setup="from __main__ import words_comp", number=10000))
    # print(timeit.timeit("words_map()", setup="from __main__ import words_map", number=10000))

    # Pass a reference to the function to timeit
    print(timeit.timeit(text_comp, number=10000))
    print(timeit.timeit(text_map, number=10000))
    print(timeit.timeit(words_comp, number=10000))
    print(timeit.timeit(words_map, number=10000))