def solution(n, h):
    c, f = ["*","*","***"], ["*"*(h if h%2 else h+1) for _ in range(n)]
    print(c,f)
    b = ["*****"+"*"*((2*j)+(i*2)) for i in range(n) for j in range(h)]
    print(b)
    return [i.rjust((len(b[-1])//2)+(len(i)-len(i)//2)," ") for i in c+b+f]