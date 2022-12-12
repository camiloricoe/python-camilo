def solution(cell1, cell2):
    return (ord(cell1[0])+int(cell1[1])) % 2 == (ord(cell2[0])+int(cell2[1])) % 2

    """
    
    mydict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    cell1=list(cell1)
    cell2=list(cell2)
    cell1[0]=mydict.get(cell1[0])
    cell2[0]=mydict.get(cell2[0])
    print(cell1,cell2)
    
    return (cell1[0]+int(cell1[1]))%2==(cell2[0]+int(cell2[1]))%2
 
    """
