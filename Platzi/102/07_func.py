def find_volume(lengh=1,width=1,depth=1):
  return lengh*width*depth

result=find_volume(10,20,10)
print(result)
result=find_volume()
print(result)
result=find_volume(width=10)
print(result)

def find_volume(lengh=1,width=1,depth=1):
  return lengh*width*depth,width,'hola'

result=find_volume(10,20,10)
print(result)
result, width, text=find_volume(10,20,10)
print(result)
print(width)
print(text)