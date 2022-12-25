def solution(a):
    count, i = 0, 0
    while i < len(a):
        if i != len(a) - 1 and a[i] >= a[i+1]:
            count += abs(a[i] - a[i+1]) + 1
            a[i+1] += a[i] - a[i+1] + 1
        print(a)
        i += 1
    return count
