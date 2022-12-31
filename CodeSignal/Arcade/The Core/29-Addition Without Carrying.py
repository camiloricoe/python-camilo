from itertools import zip_longest


def solution(p1, p2):
    res = []
    for a, b in zip_longest(str(p1)[::-1], str(p2)[::-1], fillvalue="0"):
        res.append(str((int(a)+int(b)) % 10))
    res = res[::-1]
    return int(''.join(res))
