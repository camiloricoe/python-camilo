def solution(a, b):
    res = float('inf')
    for i in set(a):
        res = min(res, b.count(i)//a.count(i))
    return res


"""
def solution(A, B):
    return min(B.count(c)//A.count(c) for c in A)
    """
