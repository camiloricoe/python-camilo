def solution(n):
    for i in str(n):
        if int(i) % 2 != 0:
            return False
    return True

#   return all([int(i)%2==0 for i in str(n)])
