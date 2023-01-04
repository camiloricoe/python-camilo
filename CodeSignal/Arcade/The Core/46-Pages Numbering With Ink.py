def solution(current, numberOfDigits):

    while True:
        ln = len(str(current))
        print(numberOfDigits, current)
        if numberOfDigits-ln >= 0:
            current += 1
            numberOfDigits -= ln
            continue

        return current-1
