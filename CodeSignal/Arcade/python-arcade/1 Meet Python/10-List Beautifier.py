def solution(a):
    res = a[:]
    while res and res[0] != res[-1]:
       a,*res,b = res
    return res


def solution(a):
    res = a[:]
    while res and res[0] != res[-1]:
        res=res[1:-1]# = res
    return res