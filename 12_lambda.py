def increment(x):
  return x + 1

print(increment(11))

increment_v2 = lambda x : x + 1
print(increment_v2(12))

full_name = lambda name, last_name : f'Full name is {name.title()} {last_name.title()}'

print(full_name('Christian', 'gutierrez'))
text = full_name('Mary', 'Ramirez')
print(text)

print((lambda x : x * 2)(3))#3 es el argumento de x