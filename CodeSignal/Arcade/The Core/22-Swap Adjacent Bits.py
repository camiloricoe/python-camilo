def solution(n):
    return sol2(n)


def sol2(n):
    n = bin(n)[2:]
    print(n)
    if len(n) % 2 != 0:
        n = "0"+str(n)
        print(n)
    x = [n[i:i+2] for i in range(0, len(n), 2)]
    print(x)
    y = [i[::-1] for i in x]
    print(y)

    return int("".join(y), 2)
