def solution(matrix):
    s = set()
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            s.add((matrix[i][j], matrix[i][j+1],
                  matrix[i+1][j], matrix[i+1][j+1]))
    return len(s)
