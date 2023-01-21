def solution(array1, array2):
    if len(array1)==len(array2):
        for i in range(len(array1)):
            if len(array1[i]) != len(array2[i]):
                return False
        return True
    return False

def solution(array1, array2):
    return [len(i) for i in array1] == [len(i) for i in array2]