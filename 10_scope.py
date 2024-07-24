price = 100 # global

def increment():
  price = 200 #local
  result = price + 10
  return result

print(price)
print(increment())

