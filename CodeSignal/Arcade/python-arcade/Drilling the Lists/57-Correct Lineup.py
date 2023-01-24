def solution(athletes):
    return slist(athletes)
    
def slist(aliust):
    for i in range(0,len(aliust),2):
        aliust[i],aliust[i+1]=aliust[i+1],aliust[i]
    return aliust
    
    
def solution(athletes):
    return [athletes[i+1] if i%2 == 0 else athletes[i-1] for i in range(0,len(athletes)) ]