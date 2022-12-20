import random

def mergesort(lista):
    if len(lista)>1:
        medio = len(lista)//2
        iz =lista[:medio]
        de =lista[medio:]

        print(iz,'-'*6,de)

        #llamda recursiva de cada mitad
        mergesort(iz)
        mergesort(de)

        i=0
        j=0
        k=0

        while i < len(iz) and j<len(de):
            if iz[i]<de[j]:
                lista[k]=iz[i]
                i+=1
            else:
                lista[k] = de[j]
                j+=1
            k+=1

        while i<len(iz):
            lista[k]=iz[i]
            i+=1
            k+=1

        while j < len(de):
            lista[k] = de[j]
            j += 1
            k += 1

        print(f'izquierda {iz}, derecha {de}')
        print(lista)
        print('-' * 50)

    return lista


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    print('-'*20)

    lista_ordenada = mergesort(lista)
    print(lista_ordenada)
