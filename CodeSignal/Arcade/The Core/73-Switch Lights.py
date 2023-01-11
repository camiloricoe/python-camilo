def solution(b):
    a = [bool(x)for x in b]
    for i in range(len(a)):
        ch = a[i:].count(1)
        if ch % 2 != 0:
            a[i] = not a[i]
    return [int(x) for x in a]


def solution(a):
    return [(x + sum(a[i:])) % 2 for i, x in enumerate(a)]
