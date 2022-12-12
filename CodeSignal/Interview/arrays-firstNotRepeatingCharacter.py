def solution(s):
    for i in s:
        if s.index(i) == s.rindex(i):
            return i

    return '_'
