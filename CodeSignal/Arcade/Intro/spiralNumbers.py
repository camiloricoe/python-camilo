def solution(n):
        
    # declare 2D array
    pattern = [[0 for i in range(n)] for j in range(n)]

    # initialize
    num = 1 # starting number
    i = 0 # 2d array row index
    j = 0 # 2d array column index
    top = 0 # to store row index lower limit 
    botton = n - 1 # to store row index upper limit 
    left = 0 # to store column index lower limit
    right = n - 1 # to store column index upper limit

    # fill the array to create patern.
    # stop when n > s * s
    while num <= n * n:
        # fill horizontally left to right
        for j in range(left, right + 1):
            pattern[top][j] = num
            num = num + 1

        # update row index lower limit
        top = top + 1

        # fill vertically top to bottom
        for i in range(top, botton + 1):
            pattern[i][right] = num
            num = num + 1

        # update column index upper limit
        right = right - 1

        # fill horizontally right to left
        for j in range(right, left - 1, -1):
            pattern[botton][j] = num
            num = num + 1

        # update row index upper limit
        botton = botton - 1
        
        for i in range(botton, top - 1, -1):
            pattern[i][left] = num
            num = num + 1

        left = left + 1
        

    return pattern

'''
def solution(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m
'''