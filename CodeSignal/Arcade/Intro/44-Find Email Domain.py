def solution(address):
    b = address.rfind('@')
    return address[b+1:]
