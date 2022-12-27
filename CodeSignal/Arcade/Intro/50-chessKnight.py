def solution(cell):
    c = ord(cell[0]) % 96
    r = int(cell[1])
    cmoves = 8
    moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),
             (2, 1), (2, -1), (-2, 1), (-2, -1)]
    for i in moves:
        cn = c+i[0]
        rn = r+i[1]
        if cn > 8 or cn < 1 or rn > 8 or rn < 1:
            cmoves -= 1

    return cmoves
