import random

dict ={}
for i in range(1,5):
  dict[i]=i*2

print(dict)

dict_v2={i:i*2for i in range(1,5)}
print(dict_v2)

countries = ['col', 'mex', 'bol','pe']
population ={}
for country in countries:
  population[country]= random.randint(1,100)

print(population)

population_v2={country:random.randint(1,100) for country in countries}
print(population_v2)

names=['nico','zule','santi']
ages = [12,56,98,100,43]

print(list(zip(names,ages)))
print(list(zip(ages,names)))

namesages={name:age for (name,age) in zip(names,ages)}
print(namesages)

# new_dict = {names[i]:edades[i] for i in range(len(names))}

namesages={name:age for (name,age) in zip(names,ages) if age<30}
print(namesages)

text = 'Hola, soy Andy y esta es una cadena de caracteres de prueba'
unique = {a: a.upper() for a in text if a in 'ndu'}
print(unique)