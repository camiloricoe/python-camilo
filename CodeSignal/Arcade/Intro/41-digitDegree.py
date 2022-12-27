def solution(n):
    steps = 0
    while n >= 10:
        n = sum([int(i) for i in str(n)])
        steps += 1
    return steps
