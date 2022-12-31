def solution(n, l, r):
    if l+r <= n:
        l = n-r
    else:
        r = n-l
    return max((r-l)//2+1, 0)


"""

def solution(n, l, r):
    sol=0
    a=l
    b=r
    
    if l+r==n and l==r:
        sol=1
        return sol
        
    if l+r<=n: 
        for i in range(l,r+1):
            if i+b==n:
                sol+=1+(b-i)//2
                return sol
        return sol
    if l+r>n:
        for i in range(r,l-1,-1):
            if i+a==n:
                sol+=1+(i-a)//2
                return sol
        return sol
    

def solution(n, l, r):
    sol=0
    if l+r==n and l==r:
        sol=1
    for i in range(r,l,-1):
        for j in range(l,i+1):
            print(i,j)
            if i+j==n:
                sol+=1
                break
            if i+j>n:
                break
    return sol
 """
