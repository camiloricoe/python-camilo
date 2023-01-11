def solution(coins, price):
    res = 0
    for i in range(1, len(coins)+1):
        coin = price//coins[-1*i]
        res += coin
        price -= coin*coins[-1*i]
        print(res, price)
        if price == 0:
            return res


def solution(coins, price):
    res = 0
    for x in reversed(coins):
        t, price = divmod(price, x)
        res += t
    return res
