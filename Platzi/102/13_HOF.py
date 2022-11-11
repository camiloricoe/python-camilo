def increment(x):
  return x + 1

def high_ord_func(x, func):
  return x + func(x)
  

increment_v2 = lambda x: x +1
high_ord_func_v2 = lambda x, func: x + func(x)


result = high_ord_func(2, increment)
# 2 + (2 + 1)
print(result)

result = high_ord_func_v2(2, increment_v2)
print(result)
result = high_ord_func_v2(2, lambda x: x + 2)
print(result)
## change
result = high_ord_func_v2(2, lambda x: x * 5)
print(result)


#Forma con lambda

#Funcion de segundo orden
a = lambda y: y + 1

#Funcion de orden superior (HOF)
b = lambda y, func: y + func(y) 

#Funcion de segundo orden como parametro de la HOF
result = b(2, a)

print(result)