file = open('./text.txt')
print(file.read())
# readline()
print(file.readline())
print(file.readline())
print(file.readline())

print('segunda opcion')
for line in file:
  print(line)

file.close()
print('tercera opcion')

with open('./text.txt') as file:
  for line in file:
    print(line)
    
# readlines()
file = open('./text.txt')
print(file.readlines())
file.close()
