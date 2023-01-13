def solution(number):
    res = []
    num = ord(number)
    for i in range((num-65)//2 + 1):
        res.append(f"{chr(65+i)} + {chr(num-i)}")
    return res
