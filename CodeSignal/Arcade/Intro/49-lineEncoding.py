def solution(s):
    prev = s[0]
    actual = ""
    acum = 1
    res = ""
    for i in range(1, len(s)):
        actual = s[i]
        if prev == actual:
            acum += 1
            prev = actual

        else:
            if acum == 1:
                res = res+prev
                prev = actual
            else:
                res = res+str(acum)+prev
                acum = 1
                prev = actual

        if i == len(s)-1:
            if acum == 1:
                res = res+actual
            if acum > 1:
                res = res+str(acum)+actual

    return res


"""
from itertools import groupby
def solution(s):
    x = ''
    for k,g in groupby(s):
        y = len((list(g)))
        if y==1:
            x += k
        else:
            x += str(y) + k
    return x
"""
