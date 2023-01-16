import re


def solution(s1, s2):
    # Break down the strings into tokens
    tokens1 = re.findall(r'[a-zA-Z]+|\d+', s1)
    tokens2 = re.findall(r'[a-zA-Z]+|\d+', s2)

    diff_lengths = len(tokens1) != len(tokens2)

    for i in range(max(len(tokens1), len(tokens2))):
        if diff_lengths:
            if i == len(tokens1):
                return True
            if i == len(tokens2):
                return False
        if re.match(r'\d+', tokens1[i]) and re.match(r'\d+', tokens2[i]):
            n1 = re.match(r'^0*(\d+)$', tokens1[i]).group(1)
            n2 = re.match(r'^0*(\d+)$', tokens2[i]).group(1)
            if n1 != n2:
                return int(n1) < int(n2)
        elif tokens1[i] != tokens2[i]:
            return tokens1[i] < tokens2[i]

    for i in range(len(tokens1)):
        if re.match(r'\d+', tokens1[i]) and re.match(r'\d+', tokens2[i]):
            leading_zeros1 = len(re.match(
                r'^[0]+', tokens1[i]).group(0)) if re.match(r'^[0]+', tokens1[i]) else 0
            leading_zeros2 = len(re.match(
                r'^[0]+', tokens2[i]).group(0)) if re.match(r'^[0]+', tokens2[i]) else 0

            if leading_zeros1 != leading_zeros2:
                return leading_zeros1 > leading_zeros2

    return False


def solution(s1, s2):
    m1 = re.findall(r'([a-z]+|[0-9]+)', s1)
    m2 = re.findall(r'([a-z]+|[0-9]+)', s2)
    l1 = [tryparse(x) for x in m1]
    l2 = [tryparse(x) for x in m2]
    c1 = [len(x) for x in m1]
    c2 = [len(x) for x in m2]
    if l1 < l2:
        return True
    if l1 == l2:
        return c1 > c2
    return False


def tryparse(x):
    if x.isdigit():
        return x.zfill(20)
    return x
