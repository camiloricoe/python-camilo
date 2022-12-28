def solution(a, b, c):
    if a+b == c or a-b == c or a*b == c or a/b == c:
        return True
    return False


"""   
def solution(a, b, c):
    return c in (a+b,a-b,a*b,a/b)
"""
