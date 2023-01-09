def solution(A, B):
    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2

def solution(A, B):
    d = [(x,y) for x,y in zip(A,B) if x!=y]
    return len(d) == 0 or (len(d) == 2 and d[0][::-1]==d[1])