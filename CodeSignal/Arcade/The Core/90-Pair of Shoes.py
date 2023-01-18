def solution(shoes):
    a = []
    b = []
    for s in shoes:
        if s[0] == 0:
            a.append(s[1])
        else:
            b.append(s[1])
    return sorted(a) == sorted(b)
