def solution(words):
    count = 0
    for i in range(4):
        ta = words[i]
        al = len(ta)
        for a in range(al - 2):
            for j in range(4):
                if j == i:
                    continue
                tb = words[j]
                jl = len(tb)
                b = tb.find(ta[a], 0, -2)
                while b != -1:
                    for b2 in range(b + 2, jl):
                        for k in range(4):
                            if k == j or k == i:
                                continue
                            l = 6 - k - i - j
                            bd = b2 - b
                            td = words[l]
                            dl = len(td)
                            if bd >= dl:
                                continue
                            tc = words[k]
                            cl = len(tc)
                            c = tc.find(tb[b2], 0, -2)
                            while c != -1:
                                if tb[b2] != tc[c]:
                                    continue
                                for c2 in range(c + 2, cl):
                                    for d in range(dl - 1, bd - 1, -1):
                                        if tc[c2] != td[d]:
                                            continue
                                        a2 = a + c2 - c
                                        if a2 >= al:
                                            break
                                        if ta[a2] == td[d - bd]:
                                            count += 1
                                c = tc.find(tb[b2], c + 1, -2)
                    b = tb.find(ta[a], b + 1, -2)
    return count


"""
def solution(words):
    from itertools import permutations as p
    c = 0
    for l in p(words):
        for d1 in range(len(l[0])-2):
            s1 = [i for i,j in enumerate(l[1]) if j == l[0][d1]]
            for d2 in range(d1+2, len(l[0])):
                s2 = [i for i,j in enumerate(l[2]) if j == l[0][d2]]
                for cw1 in s1:
                    for cw2 in s2:
                        for c1, c2 in zip(l[1][cw1+2:],l[2][cw2+2:]):
                            for c3, c4 in zip(l[3],l[3][d2-d1:]):
                                c += c1 == c3 and c2 == c4
    return c
    """
