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

prices = list(map(lambda item: item['price'], items))
print(prices)

new_items = list(map(lambda item: item | {'tax': item['price'] * .19}, items))
print(new_items)

def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items2 = list(map(add_taxes, items))
print(new_items2)