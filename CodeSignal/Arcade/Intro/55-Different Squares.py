def solution(matrix):
    cuadros = []

    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            cuadro = [matrix[i][j], matrix[i][j+1],
                      matrix[i+1][j], matrix[i+1][j+1]]
            if cuadro not in cuadros:
                cuadros.append(cuadro)
    return len(cuadros)


'''
def solution(matrix):
    s = set()
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
                s.add((matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]))
    return len(s)
    '''
