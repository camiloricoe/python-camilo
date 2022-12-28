def solution(s1, s2):
    if s1 == 7 and (s2 == 5 or s2==6):
        return True
    if (s1 ==5 or s1==6) and s2 == 7:
        return True
    if (s1==6 or s2 == 6) and (s1<5 or s2< 5):
        return True
    return False

def solution(score1, score2):
    mins, maxs = (min(score1, score2), max(score1, score2))
    return (maxs == 6 and mins < 5) or (maxs == 7 and mins in (5,6))