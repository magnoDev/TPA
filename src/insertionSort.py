def insertionsort(lista):
    for i in range(1, len(lista)):
        j = i
        while ((lista[j] < lista[j - 1]) and (j > 0)):
            aux = lista[j]
            lista[j] = lista[j - 1]
            lista[j - 1] = aux
            j = j - 1

    return lista