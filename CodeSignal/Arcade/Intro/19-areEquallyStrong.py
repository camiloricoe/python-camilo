def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return yourLeft+yourRight == friendsLeft+friendsRight and max(yourLeft, yourRight) == max(friendsLeft, friendsRight)
