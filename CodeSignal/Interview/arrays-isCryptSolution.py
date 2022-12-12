def solution(crypt, solution):
    res = {sub[0]: sub[1] for sub in solution}
    num=""
    sol=[]
    for word in range(3):
        num=""    
        for letter in crypt[word]:
            num+=res[letter]
        sol.append(num)
    print(sol)  
    for strnum in sol:
        if len(strnum)>1:
            if strnum.startswith("0") == True:
                return False
    return int(sol[0])+int(sol[1])==int(sol[2])