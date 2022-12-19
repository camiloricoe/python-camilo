def solution(inputString):
    a = list(set(inputString))
    a.sort(reverse=True)
    prev = inputString.count(a[0])
    if a[-1] != 'a':
        return False
    for i in range(len(a)-1):
        act = inputString.count(a[i+1])
        if act < prev:
            return False
        if ord(a[i])-1 != ord(a[i+1]):
            return False
        prev = act
    return True


"""
def solution(inputString):

    r = [inputString.count(i) for i in string.ascii_lowercase]
    
    return r[::-1] == sorted(r)
    
    """
