set_countries = {'col', 'mex', 'bol', 'col'}

print(set_countries)
print(type(set_countries))

set_types = {1, 'hola', False, 12.12}
print(set_types)

set_from_string = set('hola')
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
numbers_unique = list(set_numbers)
print(numbers_unique)