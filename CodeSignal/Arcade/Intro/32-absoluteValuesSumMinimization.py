def solution(a):
    minimo = float('inf')
    res = 0
    output = float('inf')
    a.sort()
    for i in a:
        res = 0
        for j in a:
            res += abs(j-i)
        if res < minimo:
            minimo = res
            output = i
    return output
