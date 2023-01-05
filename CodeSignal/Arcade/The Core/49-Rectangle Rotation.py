

def calculateRectangleArea(A, B, C):
    s = (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])) / 2
    return abs(s)


def solution(a, b):
    count = 0

    # cos and sin of 45 degree
    cos = sin = 2 ** (1 / 2) / 2

    # initial rectangle
    A = (-a / 2, b / 2)
    B = (a / 2, b / 2)
    C = (a / 2, -b / 2)
    D = (-a / 2, -b / 2)

    rectangle = [A, B, C, D]

    # rotate rectangle by 45 degree
    rectangleRot = []

    for r in rectangle:
        rt = (r[0] * cos - r[1] * sin, r[0] * sin + r[1] * cos)
        rectangleRot.append(rt)

    # vertices of outer rectangle
    xA = rectangleRot[0][0]
    yB = rectangleRot[1][1]
    xC = rectangleRot[2][0]
    yD = rectangleRot[3][1]

    # iterate over outer rectangle points
    for x in range(round(xA), round(xC) + 1):
        for y in range(round(yD), round(yB) + 1):
            # calculate areas of rectangles with each point

            area1 = calculateRectangleArea(
                rectangleRot[0], rectangleRot[1], (x, y))
            area2 = calculateRectangleArea(
                rectangleRot[1], rectangleRot[2], (x, y))
            area3 = calculateRectangleArea(
                rectangleRot[2], rectangleRot[3], (x, y))
            area4 = calculateRectangleArea(
                rectangleRot[3], rectangleRot[0], (x, y))

            # inside if areas are equal
            if abs(sum([area1, area2, area3, area4]) - a * b) < 1e-10:
                count += 1

    return count


"""
def solution(a, b):
    [m, n] = [int(math.floor(x / math.sqrt(2))) for x in (a, b)]
    return m * n + (m + 1) * (n + 1) - (m + n) % 2
    """
