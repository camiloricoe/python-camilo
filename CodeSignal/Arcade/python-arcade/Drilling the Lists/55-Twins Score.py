def solution(b, m):
    return [b[i]+m[i] for i in range(len(b))]
    # return list(map(sum, zip(b, m)))

