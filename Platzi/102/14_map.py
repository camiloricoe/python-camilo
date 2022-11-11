numbers =[1,2,3,4]
numbers_v2=[]

for i in numbers:
  numbers_v2.append(i * 2)

numbers_v3 = list(map(lambda i:i*2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers_1 =[1,2,3,4]
numbers_2 =[5,6,7]

result = list(map(lambda x, y: x+y, numbers_1,numbers_2))
print(result)


#map and dict

dict= [
    {
        'product':'camisa',
        'price':120,
    },
    {
        'product':'pantalon',
        'price':160
    },
    {
        'product':'pantalon_2',
        'price':205
    },
]


prices = list(map(lambda item:item['price'],dict))
print(prices)

# esta clase modifica el array original, porque los diccionarios estar referenciados en memoria
def add_taxes(item):
  item['taxes'] = item['price'] *.19
  return item

#esta funcion crea un nuevo diccionario para evitar el tema de referencicacion
def add_taxes(item):
  new_item=item.copy()
  new_item['taxes'] = new_item['price'] *.19
  return new_item

new_items = list(map(add_taxes,dict))
print(new_items)
print(dict)

