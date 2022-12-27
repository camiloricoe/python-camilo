def solution(min1, min2_10, min11, s):
    res = 0
    if s >= min1:
        res = 1
        s -= min1
    if s >= min2_10*9:
        res = 10
        s -= min2_10*9
    else:
        res += s//min2_10
        return res

    res += s//min11
    return res
