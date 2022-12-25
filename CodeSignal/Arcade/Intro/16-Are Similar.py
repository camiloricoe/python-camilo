def solution(A, B):
    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2