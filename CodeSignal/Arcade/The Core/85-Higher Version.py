def solution(ver1, ver2):
    regex = '\d+'                 
    match1 =ver1.split(".")
    match2 =ver2.split(".")
    print(match1, match2)
    for i in range(len(match1)):
        if int(match1[i])<int(match2[i]):
            return False
        elif int(match1[i])>int(match2[i]):
            return True
    return False
        
def solution(ver1, ver2):
    return list(map(int,ver1.split('.'))) > list(map(int,ver2.split('.')))