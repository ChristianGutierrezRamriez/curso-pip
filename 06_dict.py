import random

countries = {'col','mex','bol','pe'}
population = {countries: random.randint(1,100) for countries in countries}
print(population)

result = {countries: population for (countries, population) in population.items() if population > 50}
print(result)

text = 'Hola, soy Christian'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)
unique2 = {c: text.count(c) for c in text if c in 'aeiou'}
print(unique2)