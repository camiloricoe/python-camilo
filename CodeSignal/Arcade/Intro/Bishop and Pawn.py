def solution(bishop, pawn):
    pawn_row = int(pawn[1])
    pawn_col = ord(pawn[0]) % 96
    bishop_row = int(bishop[1])
    bishop_col = ord(bishop[0]) % 96

    if pawn_row == bishop_row or pawn_col == bishop_col:
        return False

    print(bishop_col, bishop_row, pawn_col, pawn_row)
    # check if the bishop and pawn are on the same diagonal
    # the slope of the line connecting the bishop and pawn positions should be 1 or -1
    slope = (pawn_row - bishop_row) / (pawn_col - bishop_col)
    if slope == 1 or slope == -1:
        return True
    else:
        return False
