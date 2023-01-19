from itertools import combinations

def solution(inputArray, result):
    pairs = list(combinations(inputArray, 2))
    sol=0
    
    for pair in pairs:
        for i in range(len(result)):
            print(pair,pair[0][i],pair[1][i])
            if pair[0][i]!=result[i] and pair[1][i]!=result[i]:
                break
            if i == len(result)-1:
                sol+=1
    
    return sol               