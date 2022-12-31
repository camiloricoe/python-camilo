def solution(a, b, n):
    res = 0
    for i in range(n):
        res += a*b
        a += 1
        b += 1
    return res


"""  
def solution(a, b, n):
    return sum([(a + i) * (b + i) for i in range(n)])

def solution(a, b, n):
    if not n:
        return 0
    
    return a*b + solution(a+1,b+1,n-1)
"""
