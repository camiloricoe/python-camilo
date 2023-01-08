import math
def solution(s):
    l0 = sorted([s.count(c) for c in set(s)])
    m = math.floor(math.sqrt(10 ** (len(s)) - 1))
    for i in range(m, 0, -1):
        n = str(i * i)
        l1 = sorted([n.count(c) for c in set(n)])
        if l0 == l1:
            return i * i
    return -1


"""  
def solution(s):
    counted = []
    num = []
    for i in range(0,len(s)):
        if s[i] not in counted:
            num.append(s.count(s[i]))
            counted.append(s[i])
    digits = sum(num)
    num = sorted(num)
    
    
    
    for j in range(int(math.ceil(pow(pow(10,digits),.5))),0,-1):
        sq = str(int(pow(j,2)))
        counted = []
        numSq = []
        for i in range(0,len(sq)):
            if sq[i] not in counted:
                numSq.append(sq.count(sq[i]))
                counted.append(sq[i])
        numSq = sorted(numSq)
        if num == numSq:
            return int(sq)
    
    return -1
    """
