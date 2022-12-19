def solution(s):
    if len(s) != 17:
        return False
    numbers = s.split("-")

    if len(numbers) != 6:
        return False

  # Check if each number is a valid hexadecimal number
    for number in numbers:
        try:
            int(number, 16)
        except ValueError:
            return False

    # If all checks pass, return True
    return True
