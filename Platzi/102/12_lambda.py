def increment(x):
  return x+1


result = increment(9)
print(result)


incrementv2 = lambda x : x+1
result = incrementv2(20)
print(result)

full_name = lambda name, last_name : name+' '+last_name
nombre=full_name('Camilo', 'Rico')
print(nombre)

full_name = lambda name, last_name : f'Full name is {name.title()} {last_name.upper()}'
nombre=full_name('Camilo', 'Rico')
print(nombre)