import re


def solution(text):
    wd_list = re.split('[^a-zA-Z]', text)
    ws_list_filtered = []
    for i in wd_list:
        a = list(filter(lambda x: x.isalpha(), i))
        ws_list_filtered.append("".join(a))

    return max(ws_list_filtered, key=len)


'''   
def solution(text):
    return max(re.split('[^a-zA-Z]', text), key=len)
'''
