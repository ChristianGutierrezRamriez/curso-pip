print(0 / 0)
# ZeroDivisionError: division by zero
print(result)
# NameError: name 'result' is not defined

suma = lambda x, y: x + y
assert suma(2,2) == 4
# AssertionError: assert False

age = 10
if age < 18:
  raise Exception('No se permiten menores de edad')
  