def solution(n):
    res, i = 1, 1
    while res < n:
        res *= (i+1)
        i += 1
    return res
