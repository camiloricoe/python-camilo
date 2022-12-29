def solution(a):
    c = str(bin(a).replace("0b", ""))
    return int(c[::-1], 2)


'''
def solution(a):
    return int(bin(a)[2:][::-1],2)
'''
