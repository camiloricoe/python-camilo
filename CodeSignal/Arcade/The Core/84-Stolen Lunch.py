def solution(txt):
    x = "0123456789abcdefghij"
    y = "abcdefghij0123456789"
    mytable = txt.maketrans(x, y)
    return txt.translate(mytable)
