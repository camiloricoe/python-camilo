def solution(inputArray):
    return list(filter(lambda item: len(item) == len(max(inputArray, key=len)), inputArray))