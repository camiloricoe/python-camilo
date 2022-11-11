user_1= input('piedra, papel o tijera=> ').lower()
print(user_1)
computer = 'piedra'

if user_1 == computer:
  print('Empate')
elif user_1 == 'piedra' and computer == 'tijera':
  print('Gana Usuario')
elif  user_1 == 'tijera' and computer == 'papel':
  print('Gana Usuario')
elif  user_1 == 'papel' and computer == 'piedra':
  print('Gana Usuario')  
else:
  print('Gana Maquina')
  
