def solution(n):
    area=1
    for i in range(1,n):
        area+=(n-i)*4
    return area
