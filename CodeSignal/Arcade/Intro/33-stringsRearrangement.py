from itertools import permutations


def solution(inputArray):
    a = list(permutations(inputArray))
    # se crea un alista con todas les permutaciones y se empieza a probar una a una
    for array in a:
        if testArrangement(array):
            return True
    return False


def testArrangement(array):
    for i in range(len(array) - 1):
        # con el arreglo busca verificar en las parejas cuales solo cambian 1 vez, si solo cambian 1 vez es true lo cual devuleve true lo cual hace pasar el programa
        print([a != b for a, b in zip(array[i], array[i + 1])])
        print(sum([a != b for a, b in zip(array[i], array[i + 1])]))
        if sum([a != b for a, b in zip(array[i], array[i + 1])]) != 1:
            return False
    return True
