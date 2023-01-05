def solution(L, R):
    res = 0
    for i in range(L, R+1):
        for j in range(i+1, R+1):
            if j >= i-s(i) and j <= i+s(i) and i >= j-s(j) and i <= j+s(j):
                res += 1
    return res


def s(a: int) -> int:
    return sum([int(x) for x in str(a)])


"""       

    pair = []
    pairNum = 0
    for i in range(L,R+1):
        s = 0
        temp = i
        while temp:
            s += temp%10
            temp //= 10
        for j in range(i-s,i+s+1):
            if i < j <=R:
                pair.append([i,j])
            if j < i:
                if [j,i] in pair:
                    pairNum +=1
                
    return pairNum





    res = 0
    pairs=[]
    for a in range(l,r+1):
      interval = sum([int(x) for x in str(a)])    
      for conf in range(a-interval,a+interval+1):
          pair = [conf,a]
          pair.sort()
          
          if pair in pairs:
              res+=1
          else:
              pairs.append(pair)             
    return res  
"""
