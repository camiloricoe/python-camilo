"""

def solution(value1, weight1, value2, weight2, maxW):
    if weight1+weight2<=maxW:
        return value1+value2
    if value1>value2:
        if weight1<=maxW:
            return value1
    elif weight2<=maxW:
            return value2
    elif weight1<=maxW and weight2>maxW:
        return value1
    else:    
        return 0
"""
      
def solution(value1, weight1, value2, weight2, maxW):
    return max(int(weight1<=maxW)*value1,int(weight2<=maxW)*value2,int(weight1+weight2<=maxW)*(value1+value2))