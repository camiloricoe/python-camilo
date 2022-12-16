"""
def solution(inputArray, k):
    res=0
    for i in range(len(inputArray)-k+1):
        a=sum(inputArray[i:i+k]) #too many iterations
        res=max(res,a)
    return res
 """


def solution(inputArray, k):
    maxsum = sum(inputArray[:k])
    prevsum = maxsum
    for i in range(len(inputArray)-k):
        prevsum = prevsum-inputArray[i]+inputArray[i+k]
        maxsum = max(maxsum, prevsum)
    return maxsum
