def solution(n):
    div = []
    wk = []

    for i in range(1, n+1):
        divisors = d(i)
        div.append(divisors)
        wk.append(sum([1 for i in div if i > divisors]))

    mwk = max(wk)

    return [mwk, wk.count(mwk)]


def d(n):
    return len([i for i in range(1, n+1) if n % i == 0])


"""  
def solution(n):
    d = [sum(i%j==0 for j in range(1,i+1)) for i in range(1,n+1)]
    w = [sum(j>m for j in d[:i]) for i,m in enumerate(d)]
    return [max(w),w.count(max(w))]
"""
