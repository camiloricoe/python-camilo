def solution(message):
    original = []
    sum = 0
    next_char = ""
    for i in range(len(message)):
        next_char = (ord(message[i]) - ord('a') + 26 - sum) % 26
        original.append(next_char)
        sum = (sum + next_char) % 26
    return "".join(chr(c + ord('a')) for c in original)
