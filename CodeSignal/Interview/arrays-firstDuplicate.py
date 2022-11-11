def solution(a):
    num_set = set()
    no_duplicate = -1

    for i in range(len(a)):

        if a[i] in num_set:
            return a[i]
        else:
            num_set.add(a[i])

    return no_duplicate