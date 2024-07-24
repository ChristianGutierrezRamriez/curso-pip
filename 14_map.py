numbers = [1, 2, 3, 4, 5]

# map(function, iterable)
# function: function to apply to each element of the iterable
# iterable: iterable to apply the function to
# map(function, iterable)

number_v2 = []

for item in numbers:
  number_v2.append(item * 2)

print(numbers)
print(number_v2)

numbers_v3 = list(map(lambda i: i * 2, numbers))
print(numbers_v3)

numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8]

print(numbers_1)
print(numbers_2)

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)