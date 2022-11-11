counter = 0
while counter < 20:
  counter +=1
  if counter == 15:
    break
  print(counter)
  
print("--- "*5)

while counter < 20:
  counter +=1
  if counter < 15:
    continue
  if counter % 2 == 0:
    print(" par ")
  print(counter)

print("--- "*5)

for element in range(20):
  print(element)

print("--- "*5)

for element in range(10, 20):
  print(element)
  
print("--- "*5)
my_list = [23,45,67,89,43]

for i in my_list:
  print(i)
  
print("--- "*5)
my_tuple = ('camilo', 'piedra', 'papel')

for i in my_tuple:
  print(i)

print("--- "*5)
person= {
  'name': 'Camilo',
  'last_name': 'Rico',
  'langs': ['python', 'javascript'],
  'age': 99
}

for i in person:
  print(i)

for i in person:
  print(person[i])

print("--- "*5)
for i in person:
  print(i, '=>', person[i])  

for key, value in person.items():
  print(key,'==>', value)

people = [
  {
    'name': 'nico',
    'age':20
  },
  {
    'name': 'sofi',
    'age':25
  },
  {
    'name': 'cami',
    'age':25
  }
]

for person in people:
  print(person)

for person in people:
  print('name =>',person['name']) 

  
  
people2 = [
  {
    'name': 'nico',
    'age':20
  },
  {
    'name': 'sofi',
    'age':25
  },
  {
    'name': 'cami',
    'age':25
  }
]

for person in people2:
  person['Byear'] = 2022-person['age']

print(people2)