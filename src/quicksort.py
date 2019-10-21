def quicksort(v, inicio, fim):
    i = inicio
    j = fim
    p = j//2  #pivô

    while i < j:
        while v[i] < v[p]:
            i += 1
        while v[j] > v[p]:
            j -= 1
        if i <= j:
            #trocar(v[i], v[j])
            aux = v[i]
            v[i] = v[j]
            v[j] = aux
            i += 1
            j -= 1
    if i > j:
        if inicio < j:
            quicksort(v, inicio, j)
        if i < fim:
            quicksort(v, i, fim)

    return v


# def trocar(valor1, valor2):
#     aux = valor1
#     valor1 = valor2
#     valor = aux

def quicksort(v, inicio, fim):
    i = inicio
    j = fim
    p = fim  # pivô

    if fim - inicio == 1:
        return v

    while i <= j:

        while v[i] < v[p] and i < fim:
            i += 1
        while v[j] > v[p] and j > inicio:
            j -= 1
        if i <= j:
            if j == p:
                p = i

            aux = v[i]
            v[i] = v[j]
            v[j] = aux

            if i < fim:
                i += 1

            if j > inicio:
                j -= 1

    if i > j:
        if inicio < j:
            quicksort(v, inicio, j)
        if i < fim:
            quicksort(v, i, fim)


def main():
    vector = [52, 45, 25, 31, 28, 17, 65, 35, 42, 86]
    # sel.selection(vector)
    quicksort(vector, 0, len(vector) - 1)
    print(vector)


if __name__ == '__main__':
    main()