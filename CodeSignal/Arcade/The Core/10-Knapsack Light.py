def solution(value1, weight1, value2, weight2, maxW):
    return max(int(weight1<=maxW)*value1,int(weight2<=maxW)*value2,int((weight1+weight2)<=maxW)*(value1+value2))