def solution(commands):
    com = {'L': 1, 'R': -1, 'A': 2}
    res = 0
    same = 0
    for i in commands:
        res += com[i]
        res = res % 4
        print(res)
        if res % 2 == 0:
            same += 1
    return same
