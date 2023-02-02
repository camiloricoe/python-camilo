def solution(ids, k):
    digitSum = lambda x: sum([int(digit) for digit in str(x)])

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0