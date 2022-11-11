import random
options = ('piedra', 'papel' , 'tijera')


def choose_options():
  user_choice= input('piedra, papel o tijera=> ').lower()
  while user_choice not in options:
    print('Valor incorrecto. Ingresa')
    user_choice= input('piedra, papel o tijera=> ').lower()
 
  computer_choice = random.choice(options)
  return user_choice, computer_choice


def check_rules(user_1,computer,user_wins,computer_wins):
  if user_1 == computer:
    print('Empate')
  elif user_1 == 'piedra' and computer == 'tijera':
    print('Gana Usuario')
    user_wins+=1
  elif  user_1 == 'tijera' and computer == 'papel':
    print('Gana Usuario')
    user_wins+=1
  elif  user_1 == 'papel' and computer == 'piedra':
    print('Gana Usuario')  
    user_wins+=1 
  else:
    print('Gana Maquina')
    computer_wins+=1
  return user_wins, computer_wins


def rungame():
  ronda = 1
  user_w=0
  computer_w=0
  while not(user_w or computer_w) >= 2:
    print('*'*10)
    print('Ronda',ronda)
    
    user_1, computer = choose_options()
    user_w, computer_w = check_rules(user_1, computer,user_w,computer_w)
  
    print('el computador escogio: ',computer)
    ronda+=1
    print('victorias usuario: ',user_w)
    print('victorias maquina: ',computer_w)


  
rungame()
