pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_number = sorted(numbers)
print(sorted_number)
print(numbers)

numbers.sort()  # overwrites the numbers list
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog", key=str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]

names.sort(key=str.casefold)
print(names)