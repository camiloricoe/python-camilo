def solution(names):
    name_set = []
    for name in names:
        if name not in name_set:
            name_set.append(name)
        else:
            count = 1
            flag = True
            while flag:
                x = f'{name}({count})'
                count += 1
                if x not in name_set:
                    name_set.append(x)
                    flag = False

    return (name_set)