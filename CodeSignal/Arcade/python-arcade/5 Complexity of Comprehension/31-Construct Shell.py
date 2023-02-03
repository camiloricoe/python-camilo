def solution(n):
    return [[0]*min(i,2*n-i) for i in range(1, 2*n)]
