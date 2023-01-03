def solution(arr):
    lng = len(arr)
    if lng % 2 == 0:
        middle = arr[lng//2]+arr[(lng//2)-1]
    else:
        middle = arr[lng//2]
    return middle == arr[0] == arr[-1]
