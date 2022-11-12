def solution(inputString):
    dic = {i: inputString.count(i) for i in inputString}
    res = []
    for a in dic.values():
        if a % 2 != 0:
            res.append(a)
            if len(res) > 1:
                return False
    return True

    # return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1
