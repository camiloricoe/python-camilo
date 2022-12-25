def solution(n):
    n1=str(n)[:len(str(n))//2]
    n2=str(n)[len(str(n))//2:]
    sn1 =0
    sn2 =0
    for i in n1:
        sn1+=int(i)
    for i in n2:
        sn2+=int(i)
    return sn1 == sn2