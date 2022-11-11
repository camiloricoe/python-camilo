# CRUD cREATE, rEAD, uPDATE & dELETER
# CRUD crear, leer, agredar y eliminas
numbers = [1, 2 , 3 , 4 , 5]
print([1])
numbers [-1] = 10 # cambia el ultmo por 10
print(numbers)

numbers.append(700) # agresa 700 al final de la lista
print(numbers)

numbers.insert(0, 'HOLA') # Inserta hola al inicio de la lista
print(numbers)

numbers.insert(3, 'izquiersa') # agrega el str a la izquiersa de la posicon 3
print(numbers)

# Funcionamos listas []

tasks = ['uno', 'dos', 'tres']

new_list = numbers + tasks
print(new_list)

index = new_list.index('uno') # Para sabe en que posiscion se encuntra str uno
new_list[index] = 'cuatro' # actualizar la posicion de la lista
print(new_list)

new_list.remove('cuatro') # Remueva el str cuatro
print(new_list)

new_list.pop() # Rmueve el ultimo de la lista
print(new_list)

new_list.pop(0) # elimina la posicion que le indique de la lista
print(new_list)

new_list.reverse() # Invierte la lista alrreves
print(new_list)

numbers_a = [1, 4, 6, 3]
numbers_a.sort() # Ordena la lista
print(numbers_a)

string = ['ba', 'ca', 'av']
string.sort() # Ordena los str
print(string)

res = [False]*2
print(res)