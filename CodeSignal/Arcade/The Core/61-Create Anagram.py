def solution(s, t):
    repl = 0
    for i in set(t):
        if t.count(i) > s.count(i):
            repl += t.count(i)-s.count(i)
    return repl
