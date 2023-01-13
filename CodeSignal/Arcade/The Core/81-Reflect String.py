def solution(inputString):
    return "".join([ chr(122-ord(i)%97) for i in inputString])