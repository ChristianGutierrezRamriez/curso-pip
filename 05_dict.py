dict1 = {}

for i in range(1, 11):
  dict1[i] = i * 2

print(dict1)

dict_v2={i:i*2 for i in range(1,11)}
print(dict_v2)

import random

countries={'col','mex','bol','pe'}
population={}

for countrie in countries:
  population[countrie]=random.randint(1,100)

print(population)

population2={countrie:random.randint(1,100) for countrie in countries}
print(population2)

names=['Christian','Santiago','Mateo','Mary']
ages=[34,27,27,20]
print(list(zip(names,ages)))

new_dict={name:age for (name,age) in zip(names,ages)}
print(new_dict)

new_dict2=dict(zip(names,ages))
print(new_dict2)