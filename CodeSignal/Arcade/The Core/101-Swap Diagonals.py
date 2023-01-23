def solution(matrix):
    a,b=[],[]
    for i in range(len(matrix)):
        a.append(matrix[i][i])
        b.append(matrix[i][-1-i])
    for i in range(len(matrix)):
        matrix[i][i]=b[i]
        matrix[i][-1-i]=a[i]
        
       
    return matrix

def solution(matrix):
    for i in range(len(matrix)):
        matrix[i][i], matrix[i][-i-1] = matrix[i][-i-1], matrix[i][i]
    return matrix