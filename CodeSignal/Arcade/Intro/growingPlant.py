def solution(upSpeed, downSpeed, desiredHeight):
    height = 0
    steps = 0
    while desiredHeight >= height:
        height += upSpeed
        steps += 1
        if height >= desiredHeight:
            return steps
        height -= downSpeed


"""
def solution(upSpeed, downSpeed, desiredHeight):
    if desiredHeight <= upSpeed:
        return 1
    return math.ceil((desiredHeight - upSpeed) / (upSpeed - downSpeed) + 1)
    
    """
