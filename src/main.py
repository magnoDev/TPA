from src import heap, selection


def main():
    vector = [5, 4, 3, 2, 1, 9, 8, 7, 6]

    print(vector)
    s = vector[:]
    h = vector[:]
    selection.selection_sort(s)
    heap.heap_sort(h)
    print(isSorted(s), isSorted(h))


def isSorted(vector):
    for i in range(len(vector) - 1):
        if vector[i] > vector[i + 1]:
            return False
    return True


if __name__ == '__main__':
    main()
