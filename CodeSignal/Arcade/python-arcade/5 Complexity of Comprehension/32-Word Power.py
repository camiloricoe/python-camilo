def solution(word):
    num = {char: ord(char)-96 for char in word}
    return sum([num[ch] for ch in word])
