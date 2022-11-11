print(not True)
print(not False)

# not 
print('NOT AND')
print('True and True =>', not (True and True)) # False
print('True and False =>', not (True and False)) # True
print('False and True =>', not (False and True)) # True
print('False and False =>', not (False and False)) # True

stock = input('Ingrese el numero de stock =>')
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))

