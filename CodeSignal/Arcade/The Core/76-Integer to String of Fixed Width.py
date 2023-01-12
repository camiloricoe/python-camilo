def solution(number, width):
    number = str(number)
    if width <= len(number):
        return number[-width:]
    else:
        return "0"*(width-len(number)) + number


def solution(number, width):
    return ("0"*width+str(number))[-width:]


def solution(number, width):
    return str(number).zfill(width)[-width:]
