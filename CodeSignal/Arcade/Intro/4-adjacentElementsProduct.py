def solution(inputArray):
    maxi = -1000
    for element in range(0, len(inputArray)-1):
        producto = inputArray[element]*inputArray[element+1]
        if producto > maxi:
            maxi = producto

    return maxi
