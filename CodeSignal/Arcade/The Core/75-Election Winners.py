def solution(votes, k):
    maxBeforeCast = max(votes)
    possible = 0
    if k == 0 and votes.count(maxBeforeCast) == 1:
        return 1
    for i in votes:
        if i+k > maxBeforeCast:
            possible += 1
    return possible


def solution(votes, k):
    m = max(votes)
    if k == 0:
        return 1 if len([x for x in votes if x == m]) == 1 else 0
    return len([x for x in votes if x+k > m])
