def solution(inputArray):
    return [i for i in inputArray if len(i) == len(max(inputArray, key=len))]
