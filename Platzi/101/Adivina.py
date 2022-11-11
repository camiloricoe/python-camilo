import random

numero_a_adivinar=random.randint(1,100)
numero_usuario=int(input("Adivina el numero de la computadora "))
vidas=8
while numero_usuario!=numero_a_adivinar:
   
  if numero_usuario>numero_a_adivinar:
    vidas -=1
    print("""el numero de la computadora es menor
    **********************
    Te quedan""", vidas, "vidas")
    
  else:
    vidas -=1
    print("""el numero de la computadora es mayor
    **********************
    Te quedan""", vidas, "vidas")
    
  if vidas < 1:
    print("Perdiste el numero de la computadora era:",numero_a_adivinar)    
    break 
  
  numero_usuario=int(input("Otro intento el numero de la computadora: "))
  
    
if numero_usuario==numero_a_adivinar:
  print("Ganaste el nuemro de la computadora era:",numero_a_adivinar)    

  
