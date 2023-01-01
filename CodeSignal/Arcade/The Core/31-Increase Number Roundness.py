def solution(n):
    n = str(n)
    if n.count("0") == 0:
        return False
    i = n.index("0")
    while i < len(n)-1:
        if n[i+1] != "0":
            return True
        i += 1

    return False


def solution(n):
    return '0' in str(n).rstrip('0')
