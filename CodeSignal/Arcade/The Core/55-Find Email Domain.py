def solution(address):
    x = address.rindex("@")
    return address[x+1:]
