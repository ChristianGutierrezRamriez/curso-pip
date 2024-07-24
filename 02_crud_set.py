set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)

print(size)

print('col' in set_countries)
print('pe' in set_countries)

set_countries.add('pe')
print(sorted(set_countries))
set_countries.add('pe')
print(set_countries)#solo se agrega una vez

set_countries.update({'ar', 'ecua', 'pe'})

set_countries.remove('col')
print(set_countries)
set_countries.remove('ar')
print(set_countries)

set_countries.discard('arg')#este metodo elimina un elemento, pero si no exite no pasa nada

set_countries.add('arg')
print(set_countries)
set_countries.clear()#limpia todo el conjunto