def solution(s1, s2):
    mytable = s1.maketrans(s1, s2)
    c = s1.translate(mytable)
    return s2 == c and len(set(s1)) == len(set(s2))


'''
def solution(string1, string2):
    return len(set(zip(string1, string2))) == len(set(string1)) == len(set(string2))
    '''
