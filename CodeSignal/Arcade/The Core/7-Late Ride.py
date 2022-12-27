def solution(n):
    return (n//60)//10+(n//60) % 10+(n % 60)//10+(n % 60) % 10
'''   
def solution(n):
    return sum(map(int, str(n // 60 * 100 + n % 60)))
'''