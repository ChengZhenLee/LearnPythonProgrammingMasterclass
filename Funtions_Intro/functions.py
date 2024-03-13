def multiply(x, y):
    """
    Multiplies two numbers together

    Arguments:
        x -- The first number to be multiplied with
    
        y -- The second number to be multiplied with
    
    return:
        The result of the multiplication
    """
    result = x * y
    return result

def is_palindrome(string):
    """
    Check if a string with upper and lower
    case characters is a palindrome

    Arguments:
        string -- The string with upper and lower case characters that is checked

    return:
        True if it is a palindrome, false if not
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    """
    Check if a sentence with punctuation 

    Arguments:
        sentence -- A string with punctuation, 
        lower and upper case characters that is checked

    Returns:
        True if it is a palindrome, false if not
    """
    scrubbed_sentence= ""
    for char in sentence:
        if char.isalnum():
            scrubbed_sentence += char
    
    # return scrubbed_sentence[::-1] == scrubbed_sentence
    return is_palindrome(scrubbed_sentence)


answer = multiply(18 ,3)
print(answer)

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
