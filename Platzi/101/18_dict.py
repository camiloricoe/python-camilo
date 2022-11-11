thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(len(thisdict))
print(thisdict["brandd"])
print(thisdict.get("brand"))
print(thisdict.get("marca"))
# print(thisdict["oscmaklc"]) da un error y detiene la operacion

print('avion' in thisdict)
print('Mustang' in thisdict)
print('model' in thisdict)
print('mkdmvs' in thisdict)


# insercion y actualizacion 
print("--- "*5)
person= {
  'name': 'Camilo',
  'last_name': 'Rico',
  'langs': ['python', 'javascript'],
  'age': 99
}

print(person)

person['name']='Camilo Andres'
person['age']-=50
person['langs'].append('rust')
print(person)
del person['last_name']
person.pop('age')
print(person)

print("--- "*5)

print(person.items())
print(person.keys())
print(person.values())
print(person.clear())

