import timeout


@timeout.timeout(900)
def run(V):
    insertionSort(V)


def insertionSort(lista):
    for i in range(1, len(lista)):
        j = i
        while ((lista[j].uid < lista[j - 1].uid) and (j > 0)):
            aux = lista[j]
            lista[j] = lista[j - 1]
            lista[j - 1] = aux
            j = j - 1

    return lista
