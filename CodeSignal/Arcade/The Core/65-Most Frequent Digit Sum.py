from collections import Counter


def solution(n):
    a = []
    while n > 0:
        a.append(sum([int(i) for i in str(n)]))
        n -= a[-1]
    b = sorted(a, reverse=True)
    return max(b, key=b.count)
