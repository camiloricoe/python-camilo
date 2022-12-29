def solution(a, b):
    c = [bin(num) for num in range(a, b+1)]
    return "".join(c).count("1")


'''
def solution(a, b):
    return sum(bin(x).count('1') for x in range(a, b+1))
'''
