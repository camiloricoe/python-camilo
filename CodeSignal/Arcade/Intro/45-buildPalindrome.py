def solution(s):
    if s == s[::-1]:
        return s
    else:
        for i in range(len(s)+1):
            if s[i:] == s[:i-1:-1]:
                return s + s[:i][::-1]
        return None
