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


def morral(tamano,pesos,valores,n):
    if n ==0 or tamano ==0:
        return 0
    if pesos[n-1]>tamano:
        return morral(tamano,pesos,valores,n-1)

    return max(valores[n-1]+morral(tamano-pesos[n-1], pesos, valores, n-1), morral(tamano, pesos, valores, n-1))


def solution(value1, weight1, value2, weight2, maxW):
    return morral(maxW,[weight1,weight2],[value1,value2],2)

"""
      
def solution(value1, weight1, value2, weight2, maxW):
    return max(int(weight1<=maxW)*value1,int(weight2<=maxW)*value2,int(weight1+weight2<=maxW)*(value1+value2))