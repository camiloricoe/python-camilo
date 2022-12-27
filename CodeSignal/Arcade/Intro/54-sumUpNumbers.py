def solution(inputString):
    n_list = re.findall(r'\d+', inputString)
    return sum(list(map(int, n_list)))
