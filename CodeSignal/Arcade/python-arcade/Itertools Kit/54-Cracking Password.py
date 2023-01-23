from itertools import product

def solution(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted([createNumber(i) for i in list(product(digits,repeat = k))if int(createNumber(i))%d==0])
    
    
"""    
sorted([createNumber(i) for i in list(permutations(digits,k)) if int(createNumber(i))%d==0])
"""