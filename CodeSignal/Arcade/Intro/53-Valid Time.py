import re


def solution(time):
    regex = re.compile("(2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])")
    return bool(regex.match(time))


"""
def solution(time):
    h,m=map(int,time.split(":"))
    return 0<=h<24 and 0<=m<60
"""
