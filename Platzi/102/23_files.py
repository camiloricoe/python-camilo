file = open('./text.txt')
print(file.read())
print("---"*5)
#despues de leerlo no lo vuleve a lear por lineas
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

print("---"*5)

file = open('./text.txt')
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

print("---"*5)

file = open('./text.txt')
for line in file:
  print(line)

file.close()

# write

print("Write","---"*5,"\n")

file = open('./text.txt','w+') #w+ borra y rescrib etodo el documento r+ lee y perimite escriir en el documento
for line in file:
  print(line)
file.write('\nnuevas cosas en u\n')
file.write('nuevas cosas en u2\n')
file.write('nuevas cosas en u3\n')
print(file.read())
file.close()

file = open('./text.txt','w+')
for line in file:
  print(line)
file.write('\nnuevas cosas en u\n')
file.write('nuevas cosas en u2\n')
file.write('nuevas cosas en u3\n')
print(file.read())
file.close()