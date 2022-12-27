def solution(deposit, rate, threshold):
    years = 0
    while deposit < threshold:
        deposit = deposit*(1+rate/100)
        print(deposit)
        years += 1
    return years
