def solution(s1, s2):
    s1d={letter:s1.count(letter) for letter in s1 }
    s2d={letter:s2.count(letter) for letter in s2 }
    sol=0
    for letter in set(s1d.keys()):
        if letter in s1d and letter in s2d:
            sol+=min(s1d[letter],s2d[letter])
    return sol