def solution(y, b, l):
    return (y and b and not l) or (l and (not y or not b))
