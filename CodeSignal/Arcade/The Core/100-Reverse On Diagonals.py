def solution(matrix):
    a,b=[],[]
    for i in range(len(matrix)):
        a.append(matrix[i][i])
        b.append(matrix[-1-i][i])
    for i in range(len(matrix)):
        matrix[i][i]=a[-1-i]
        matrix[-1-i][i]=b[-1-i]
        
       
    return matrix

def solution(m):
    for i in range(len(m) // 2):
        m[i][i],m[-i-1][-i-1]=m[-i-1][-i-1],m[i][i]
        m[i][-i-1],m[-i-1][i]=m[-i-1][i],m[i][-i-1]
    return m