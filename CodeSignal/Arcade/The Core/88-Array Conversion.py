def solution(inputArray):
    i = 1
    while len(inputArray) > 1:
        if i % 2 != 0:
            inputArray = [inputArray[i] + inputArray[i+1]
                          for i in range(0, len(inputArray), 2)]
            i += 1
        else:
            inputArray = [inputArray[i] * inputArray[i+1]
                          for i in range(0, len(inputArray), 2)]
            i += 1
    return inputArray[0]

