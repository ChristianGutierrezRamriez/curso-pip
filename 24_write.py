with open('./text.txt', 'r+') as file:
  for line in file:
    print(line)
  file.write('\nnueva linea')

#r+ permite leer y escribir en el archivo
#w+ permite leer y escribir sobre el archivo
#a+ permite leer y escribir al final del archivo
