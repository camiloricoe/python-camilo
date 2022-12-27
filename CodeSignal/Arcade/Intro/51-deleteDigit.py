def solution(n):
    maxim = 0
    strn = str(n)
    for i in range(len(strn)):
        num = int(strn[:i]+strn[i+1:])
        maxim = max(maxim, num)

    return maxim
