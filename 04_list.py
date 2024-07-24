numbers = []

for number in range(1, 11):
  numbers.append(number * 2)

print(numbers)

numbers_2 = [number for number in range(1, 11)]
print(numbers_2)

numbers_3 = [number * 2 for number in range(1, 11)]
print(numbers_3)

numbers_4 = []

for number in range(1, 101):
  if number % 2 == 0:
    numbers_4.append(number * 2)

print(numbers_4)

numbers_5 = [number * 2 for number in range(1, 101) if number % 2 == 0]
print(numbers_5)