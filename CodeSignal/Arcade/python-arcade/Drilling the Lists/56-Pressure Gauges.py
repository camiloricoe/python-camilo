def solution(morning, evening):
    return [list(map(min, zip(morning, evening))), list(map(max, zip(morning, evening)))]


