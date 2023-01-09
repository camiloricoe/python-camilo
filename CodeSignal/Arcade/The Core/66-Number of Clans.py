def solution(divisors, k):
    clans = [0] * 1024
    c = 0
    for i in range(1, k+1):
        c = 0
        for j in range(len(divisors)):
            if i % divisors[j] == 0:
                c = c | (1 << j)
        clans[c] = 1
    return sum(clans)
