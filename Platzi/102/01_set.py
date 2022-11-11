
# no tiene un par key-value, así me doy cuenta que es un set, un conjunto.
set_countries = {'col', 'mex', 'bol'}
print (set_countries)

# si yo pongo algo repetido, él me lo quita al imprimir
set_countries2 = {'col', 'mex', 'bol', 'col'}
print (set_countries2) # {'col', 'mex', 'bol'}

# puede ser mixto. El set se ordena solo, lo importante es lo que tengo dentro.
set_types = {1, 'hola', False, 12.12}
print(set_types) # {False, 1, 12.12, 'hola'}

# la podemos crear a partir de un string
set_from_string = set('hoola')
print (set_from_string) # {'a', 'l', 'o', 'h'}

# la podemos crear a partir de una tupla
set_from_tuples = set (('abc','cbv','as','abc'))
print (set_from_tuples) # {'as', 'abc', 'cbv'}

# la podemos crear a partir de una lista
numbers = [1,2,3,1,2,3,4]
set_numbers= set(numbers)
print (set_numbers) # {1, 2, 3, 4}
# si quiero convertir este set único a una lista, lo puedo hacer:
unique_numbers = list(set_numbers)
print (unique_numbers)

set_countries = {'col', 'mex', 'bol'}




# conocer el tamaño del conjunto
size = len(set_countries)
print(size) # 3

print('col' in set_countries) # True
print('pe' in set_countries) # False

# add
set_countries.add('pe')
print(set_countries) # {'col', 'mex', 'bol', 'pe'}
set_countries.add('pe')
print(set_countries) # {'col', 'mex', 'bol', 'pe'}

# update, lo que hace es sumar elementos a los existentes
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries) # {'col', 'mex', 'bol', 'pe', 'ar', 'ecua'}

# remove

set_countries.remove('col')
print(set_countries) # {'mex', 'bol', 'pe', 'ar', 'ecua'}

# si le doy remove a un elemento que no existe, 
# lanza un error python, 
set_countries.remove('ar')

# para eso usamos discard, si no existe, no falla.
set_countries.discard('arg')
print(set_countries)
set_countries.add('arg')
print(set_countries)

# limpiar todo el conjunto, lo deja en vacío
set_countries.clear()
print(set_countries)
print(len(set_countries))



set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# unión de los elementos
set_c = set_a.union(set_b)
print(set_c) # {'col', 'mex', 'bol', 'pe'}
print(set_a | set_b)  # {'col', 'mex', 'bol', 'pe'}

# obtener los elementos en común
set_c = set_a.intersection(set_b)
print(set_c) # {'bol'}
print(set_a & set_b)  # {'bol'}

# dejamos sólo los elementos de A
set_c = set_a.difference(set_b)
print(set_c)  # {'col', 'mex'}
print(set_a - set_b)  # {'col', 'mex'}

# es hacer una unión, sin los elementos en común
set_c = set_a.symmetric_difference(set_b)
print(set_c) # {'col', 'mex', 'pe'}
print(set_a ^ set_b) # {'col', 'mex', 'pe'}