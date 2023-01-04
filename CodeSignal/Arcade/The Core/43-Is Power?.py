def solution(n):
    for i in range(2, 10):
        if str(round(n**(1/i), 2))[-1] == "0":
            return True
    return False
