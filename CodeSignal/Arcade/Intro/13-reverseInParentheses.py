def solution(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            print(s[:start] + s[start+1:end][::-1] + s[end+1:])
            b=solution(s[:start] + s[start+1:end][::-1] + s[end+1:])
            return b
    return s
 