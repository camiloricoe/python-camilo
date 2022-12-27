def solution(inputArray, k):
    return [inputArray[i] for i in range(len(inputArray)) if (i+1)%k!=0 ]