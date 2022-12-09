def solution(inputArray):
    sol = 0
    for i in range(len(inputArray)-1):
        if abs(inputArray[i]-inputArray[i+1]) > sol:
            sol = abs(inputArray[i]-inputArray[i+1])
    return sol
