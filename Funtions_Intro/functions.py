def multiply(x: float, y: float) -> float:
    """
    Multiplies 2 numbers.

    Although this function is intednded to multiply 2 numbers, 
    you can also use it to multiply a sequence. If you pass a
    string, for example, as the first argument, you'll get the
    string repeated `y` times as the returned value.

    Arguments:
        x -- The number to multiply `y` with
    
        y -- The number to multiply `x` with
    
    return:
        The product of `x` and `y`
    """
    result = x * y
    return result

def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    Arguments:
        string -- The string to check.

    return:
        True if `string` is a palindrome, False otherwise
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome

    The function ignores whitespace, capitalisation and punctuation
    in the sentence 

    Arguments:
        sentence -- The sentence to check.

    Returns:
        True if `sentence` is a palindrome, False otherwise
    """
    scrubbed_sentence= ""
    for char in sentence:
        if char.isalnum():
            scrubbed_sentence += char
    
    # return scrubbed_sentence[::-1] == scrubbed_sentence
    return is_palindrome(scrubbed_sentence)


def fibonacci(n: int) -> int:
    """
    Return the `n` th Fibonacci number, for positive `n`.
    """
    if 0 <= n <= 1:
        return n
    
    n_minus1, n_minus2 = 1, 0

    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
        
    return result


for i in range(36):
    print(i, fibonacci(i))

answer = multiply(18 ,3)
print(answer)

p = palindrome_sentence()

# sentence = input("Please enter a sentence to check: ")
# if palindrome_sentence(sentence):
#     print("'{}' is a palindrome".format(sentence))
# else:
#     print("'{}' is not a palindrome".format(word))


# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

# answer = multiply(10.5, 4)
# print(answer)

# forty_two = multiply(6, 7)
# print(forty_two)

# print()

# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)
