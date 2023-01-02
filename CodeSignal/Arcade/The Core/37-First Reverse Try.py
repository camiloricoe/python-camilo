def solution(arr):
    if len(arr) <= 2:
        arr.reverse()
        return arr
    return [arr[-1]]+arr[1:-1:1]+[arr[0]]


def solution(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]
    return arr
