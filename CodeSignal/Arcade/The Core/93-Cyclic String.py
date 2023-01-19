def solution(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if s in sub * 15:
                return len(sub)

