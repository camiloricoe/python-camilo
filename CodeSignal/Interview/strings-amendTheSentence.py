def solution(s):
    a = []
    for ch in s:
        if ch.isupper():
            a.append(" "+ch.lower())
        else:
            a.append(ch)
    return ''.join(a).lstrip(' ')
