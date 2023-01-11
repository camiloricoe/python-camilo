import re
def solution(maxLength, text):
    wd_list = re.split('[^a-zA-Z]', text)
    return len(list(filter(lambda x: 0<len(x)<=maxLength, wd_list)))