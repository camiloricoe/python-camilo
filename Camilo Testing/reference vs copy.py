import copy

# only assaign is reference to the memory
a = ['Wes', 'Sarah', 'Ryan', 'Poppy']
b=a #is referring to the original array
b[0]='Camilo'
print(a,b)

a = [1, 2, 3]

def func(input_list):
    input_list[2] = 11
    return input_list

b = func(a)
print("list a:", a)
print("list b:", b)
a = [1, 2, 3]
b = a
print("address of a:", id(a))
print("addrss of b", id(b))


#copy no at second level
a = [1, 2, 3]
b = copy.copy(a)
b[2] = 11

print("list a:", a)
print("list b:", b)
print("address of a:", id(a))
print("addrss of b", id(b))

a = [1, 2, [1, 2]]
b = copy.copy(a)
b[2][0] = 11

print("list a:", a)
print("list b:", b)
print("address of a[2]:", id(a[2]))
print("address of b[2]:", id(b[2]))

#deepcopy no reference at all
a = [1, 2, [1, 2]]
b = copy.deepcopy(a)
b[2][0] = 11

print("list a:", a)
print("list b:", b)

print("address of a[2]:", id(a[2]))
print("address of b[2]:", id(b[2]))
