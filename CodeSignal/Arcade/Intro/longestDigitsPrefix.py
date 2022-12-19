def solution(inputString):
    for i in range(len(inputString)):
        if inputString[i].isdigit() == False:
            return inputString[:i]
    return inputString
