def solution(s):
    for i in range(len(s)-1):
        if ord(s[i+1]) <= ord(s[i]):
            return False
    return True
