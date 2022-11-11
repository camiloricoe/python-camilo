price = 100 #global

def printp():
  print(price)

printp()

#asignacion nueva en un nuevo contexto # local
def increment():
  price = 200
  price = price +10
  print(price)
  return price
  
# result no se puede usar fuera de este contexto
def increment():
  price = 200
  result = price +10
  print(result)
  return result

# print(result) da un error
print(price)
increment()