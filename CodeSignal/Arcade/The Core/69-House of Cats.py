def solution(legs):
    res = []
    while legs >= 0:
        res.append(legs/2)
        legs = legs-4

    return sorted(res)
