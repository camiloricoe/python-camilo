def solution(k):
    res = 0
    for i in range(k):
        if (i+1) % 2 == 0:
            res += (i+1)*(i+1)
        else:
            res -= (i+1)*(i+1)

    return res
