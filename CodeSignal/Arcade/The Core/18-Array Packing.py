def solution(a):
    b = [bin(i) for i in reversed(a)]
    b = [i.replace("0b", "") for i in b]
    c = [('0'*(8-len(i)))+str(i) for i in b if len(i) <= 8]
    return int("".join(c), 2)


'''
def solution(a):
    return sum([a[i] << i*8 for i in range(len(a))])
    
def solution(a):
    return int.from_bytes(a, 'little')
    '''
