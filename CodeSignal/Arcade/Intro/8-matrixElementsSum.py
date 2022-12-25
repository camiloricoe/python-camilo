def solution(matrix):
    matrixt = list(map(list, zip(*matrix)))
    res = 0
    for colum in matrixt:
        for item in colum:
            if item == 0:
                break
            res+=item
    return res