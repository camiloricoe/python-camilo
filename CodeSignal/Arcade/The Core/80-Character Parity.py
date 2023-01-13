def solution(symbol):
    try:
        if int(symbol) % 2 == 0:
            return "even"
        else:
            return "odd"
    except ValueError:
        return "not a digit"


def solution(s):
    return "not a digit" if not s.isdigit() else "odd" if int(s) % 2 else "even"
