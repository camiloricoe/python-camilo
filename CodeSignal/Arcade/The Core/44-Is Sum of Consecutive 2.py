"""

def solution(n):
    count = 0
    for start in range(1, n):
        end = start
        total = 0
        while total < n:
            total += end
            end += 1
        if total == n:
            count += 1
    return count


"""


def solution(n):
    res = 0
    for i in range(1, n):
        acu = 0
        end = i
        while acu <= n:
            acu += end
            if acu == n:
                res += 1
                break
            if acu > n:
                acu = 0
                break
            end += 1

    return res
