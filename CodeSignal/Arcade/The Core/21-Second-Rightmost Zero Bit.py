def solution(n):
    return 2**(len(bin(n)[2:])-1-bin(n)[2:].rindex("0", 0, bin(n)[2:].rindex("0")))

'''   
def solution(n):
    return 2**([i for i, ltr in enumerate(bin(n)[:1:-1]) if ltr == '0'])[1];
    '''
    
    