def solution(a):
    b=list(a)
    b.sort()
    ind=0
    i=0
    #print(b,a, len(a),i,ind,a[i],b[ind])
    while i<len(a) and ind<len(b):
        if b[ind] == -1:
            ind+=1
            if ind == len(b):
                break
            continue
        if a[i] == -1:
            i+=1
            if i == len(a):
                break
            continue
        a[i]=b[ind]
        i+=1
        ind+=1
    return a