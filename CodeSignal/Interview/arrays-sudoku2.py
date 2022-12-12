def solution(grid):
    sol = True
    for row in grid:
        sol = len(row) == len(set(row))+row.count('.')-1
        if sol == False:
          return sol
    gridt = list(map(list, zip(*grid)))
    for colum in gridt:
        sol = len(colum) == len(set(colum))+colum.count('.')-1
        if sol == False:
          return sol
    subs = []
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            subs.append([grid[r][c] for r in range(i, i+3)
                        for c in range(j, j+3)])
    for group in subs:
        sol = len(group) == len(set(group))+group.count('.')-1
        if sol == False:
          return sol

    return sol
