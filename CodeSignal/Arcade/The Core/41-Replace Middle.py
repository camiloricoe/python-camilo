def solution(arr):
    lng = len(arr)
    if lng % 2 == 0:
        middle = arr[lng//2]+arr[(lng//2)-1]
        return arr[0:(lng//2)-1]+[middle]+arr[(lng//2)+1:]
    else:
        return arr
