inputs = input("Please enter three numbers")

numbers = inputs.split(",")

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

result = numbers[0] + numbers[1] - numbers[2]

print(result)