def solution(cipher):
    num = ""
    res = []
    for i in cipher:
        num = num+i
        if int(num) > 96:
            res.append(chr(int(num)))
            num = ""
    return "".join(res)


def solution(cipher):
    cipher = cipher.replace('97', '097').replace(
        '98', '098').replace('99', '099')
    return ''.join(chr(int(cipher[i:i+3])) for i in range(0, len(cipher), 3))
