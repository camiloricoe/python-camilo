def solution(f1, f2):
    f1u = f1.upper()
    f1l = f1.lower()
    f2u = f2.upper()
    f2l = f2.lower()

    return (f1 > f2 and (f1u < f2u or f1l < f2l)) or (f1 < f2 and (f1u > f2u or f1l > f2l))


"""
def solution(filename1, filename2):
    return (filename1.upper() < filename2.upper()) != (filename1 < filename2)
"""
