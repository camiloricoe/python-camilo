def isprime(num):
  if num == 1:
        return False
  else:
    fac=1
    for i in range(1,num):
      fac=fac*i
    fac+=1    
    if fac % num == 0:
      return True
    else:
      return False

num=int(input("ingresa el numero "))
print(isprime(num))
    
  
  
  