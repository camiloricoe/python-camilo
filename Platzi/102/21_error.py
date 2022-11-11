import numpy

# print(0 / 0)
# print(result)
print('Hola')

suma = lambda x,y: x + y
assert suma(2,2) == 4 #los assert se utilizan para verificar, que los metodos funciona como  deberian

print('Hola 2')

'''
age = 10
if age < 18:
  raise Exception('No se permiten menores de edad')

print('Hola 3')

'''

res= lambda n,m: [[0]*n for i in range(m)]
print(res(2,2))


try:
  assert res(3,2) ==  [[0,0,0],[0,0,0]], 'res no devuelve lo deseado'
except  AssertionError as error:
  print(error)

try:
  print(0 / 0)
except ZeroDivisionError as error:
  print(error)

print('Hola')
print(res(3,2))



#tambien se pueden unir los try catch

try:
  print(0 / 0) #como ya hay un error detiene todo lo del bloque pero no falla y sigue
  assert res(3,2) ==  [[0,0,0],[0,0,2]], 'res no devuelve lo deseado'
except  AssertionError as error:
  print(error) #aqui se puede agregar logica para solucionar el erro
except ZeroDivisionError as error:
  print(error)

print('Hola')
print(res(3,2))