import math


def solution(candlesNumber, makeNew):
    res = candlesNumber
    candlesleft = candlesNumber
    sinquemar = 0
    while candlesleft >= 1:
        print(res, candlesleft, sinquemar)
        candlesleft, sinquemar = quemar(candlesleft, sinquemar, makeNew)
        res += candlesleft
        print(res, candlesleft, sinquemar)
    return res


def quemar(a, b, makeNew):
    new = (a+b)//makeNew
    sinquemar = (a+b) % makeNew
    return new, sinquemar


def solution(solutionNumber, makeNew):
    burned = parts = 0
    available = solutionNumber
    while available > 0:
        burned += 1
        available -= 1
        parts += 1
        if parts == makeNew:
            parts = 0
            available += 1
    return burned


'''
def solution(candlesNumber, makeNew):
    res=0
    remain=0
    while candlesNumber>=1:
        res+=candlesNumber
        remain+=candlesNumber%makeNew
        print(res,remain,candlesNumber)
        if remain >= makeNew:
            res+=remain//makeNew
            remain=remain%makeNew
        print(res,remain,candlesNumber)
        candlesNumber=candlesNumber//makeNew
    return res
 '''
