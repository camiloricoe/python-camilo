def solution(items):
    extended_items = [-1] + items
    previous_less = []
    for i in range(1, len(extended_items)):
        j = i - 1
        while extended_items[j] >= extended_items[i]:
            j -= 1
        previous_less.append(extended_items[j])
    return previous_less
