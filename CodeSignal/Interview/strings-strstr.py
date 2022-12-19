

"""
Avoid using built-in functions to solve this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.


def solution(s, x):
    if x in s:
        return s.index(x)
    else:
        return -1
     """


def solution(s, x):
    if x in s:
        for i in range(len(s)-len(x)+1):
            if s[i:i+len(x)] == x:
                return i
    else:
        return -1
