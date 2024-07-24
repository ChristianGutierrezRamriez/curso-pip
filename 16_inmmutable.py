items = [
  {
    'product': 'camisa',
    'price': 100
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]


def add_taxes(item):
  new_item = item.copy()#copia el diccionario, esto se hace por que si no se hace la copia, se modifica el diccionario original
  new_item['taxes'] = new_item['price'] * .19
  return new_item

new_items = list(map(add_taxes, items))
print(f'new list: {new_items}')
print(f'old list: {items}')
