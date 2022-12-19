def solution(votes, k):
    maxBeforeCast = max(votes)
    possible = 0
    if k == 0 and votes.count(maxBeforeCast) == 1:
        return 1
    for i in votes:
        if i+k > maxBeforeCast:
            possible += 1
    return possible
