def solution(inputArray):
    for lenJump in range(1, max(inputArray)+2):
        a = 0
        while a not in inputArray:
            a += lenJump
            if a > max(inputArray):
                return lenJump
