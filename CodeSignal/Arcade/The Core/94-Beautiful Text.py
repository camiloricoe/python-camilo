def solution(inputString, l, r):
    a=[(len(inputString)-i)/(i+1) for i in range(inputString.count(" ")+1) if ((len(inputString)-i)/(i+1)).is_integer()]
    print(a)
    for i in a:
        print(i,l<=i<=r,i.is_integer())
        if  l<=i<=r and i.is_integer():
            if inputString[int(i)]==" ":
                return True
    return False
        


def solution(inputString, l, r):
    for w in range(l, r+1):
        i = w
        while i < len(inputString):
            if inputString[i] != ' ':
                break
            i += w+1
        if i == len(inputString):
            return True
    return False
