try:
  print(0/0)
except ZeroDivisionError as error:
  print('Eres una burra')

print('Hola')
try:
  assert 1 != 1, 'Uno no es igual'
except AssertionError as error:
  print(error) 

print('Hola 2')

age = 10
try:
  if age < 18:
    raise Exception('No se permiten menores de edad verificquen su edad')
except Exception as error:
  print(error)

print('Hola 3')

try:
  print(0/0)
  assert 1 != 1, 'Uno no es igual'
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
  print('Eres una burra')
except AssertionError as error:
  print(error) 
except Exception as error:
  print(error)

print('Hola 3')
