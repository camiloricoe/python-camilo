def solution(startTag):
    x = startTag.split()
    y = x[0].strip("<>")
    return "</"+y+">"
