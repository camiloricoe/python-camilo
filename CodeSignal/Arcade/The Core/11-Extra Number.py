"""
def solution(a, b, c):
    if a!=b and a!=c:
        return a
    elif a==b:
        return c
    else:
        return b
"""     

def solution(a, b, c):
    return a ^ b ^ c #XOR