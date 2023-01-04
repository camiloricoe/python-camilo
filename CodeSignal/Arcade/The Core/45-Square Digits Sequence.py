def solution(a0):
    occu = []
    a = a0
    while True:
        occu.append(a)
        an = 0
        for i in str(a):
            an += int(i)**2
        a = an
        if a in occu:
            return len(occu)+1


"""
def solution(a0):
    seq = [a0]
    while seq[-1] not in seq[:-1]:
        seq.append(sum(int(i)**2 for i in str(seq[-1])))
    return len(seq)
    
"""
