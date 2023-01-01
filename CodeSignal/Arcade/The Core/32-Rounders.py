def solution(n):
    ln = len(str(n))-1
    for i in range(ln+1):
        if n % 10**i >= (10**i)/2:
            print(((n//10**i)+1)*10**i)
            n = (((n//10**i)+1)*10**i)
        else:
            print(((n//10**i))*10**i)
            n = (((n//10**i))*10**i)

    return n
