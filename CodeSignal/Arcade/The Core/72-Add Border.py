def solution(picture):
    a = len(picture[0])
    picture = ['*'+i+'*' for i in picture]
    return ['*'*(a+2)]+picture+['*'*(a+2)]
