text = "Ella sabe Python"
print(text[0])
print(text[1])
# print(text[100]) #error

print(text[len(text)-1])
print(text[-1]) #devuelve el ultimo caracter

# Slicing
print("--- "*5)

print(text[0:5])
print(text[10:999])
print(text[:10])
print(text[5:])
print(text[5:-1])

print(text[10:16:2]) # de donde a donde y paso

print(text[::2])


