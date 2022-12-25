def solution(matrix):

    # create a new matrix to hold the result
    result = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

    # iterate over each cell in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # initialize a counter for the number of mines in the neighboring cells
            count = 0

            # check the adjacent cells (up, down, left, right, and the four diagonal cells)
            # and increment the counter if the cell contains a mine
            if i > 0 and matrix[i-1][j]:
                count += 1  # up
            if i < len(matrix)-1 and matrix[i+1][j]:
                count += 1  # down
            if j > 0 and matrix[i][j-1]:
                count += 1  # left
            if j < len(matrix[0])-1 and matrix[i][j+1]:
                count += 1  # right
            if i > 0 and j > 0 and matrix[i-1][j-1]:
                count += 1  # top-left
            if i > 0 and j < len(matrix[0])-1 and matrix[i-1][j+1]:
                count += 1  # top-right
            if i < len(matrix)-1 and j > 0 and matrix[i+1][j-1]:
                count += 1  # bottom-left
            if i < len(matrix)-1 and j < len(matrix[0])-1 and matrix[i+1][j+1]:
                count += 1  # bottom-right

            # set the result matrix cell to the count of mines in the neighboring cells
            result[i][j] = count

    return result
