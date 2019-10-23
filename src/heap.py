import math
from data import Data

import timeout


@timeout.timeout(900)
def run(data):
    heap_sort(data)


## http://wiki.icmc.usp.br/images/c/c6/Ordenacao2.pdf

def heap_sort(vector):
    heapsize = len(vector)

    build_heap(vector, heapsize)
    for i in range(heapsize - 1, -1, -1):
        swap(vector, 0, i)

        heapfy(vector, i, 0)


def build_heap(vector, heapsize):
    for i in range(math.floor(heapsize / 2), -1, -1):
        heapfy(vector, heapsize, i)


def heapfy(vector, heapsize, i):
    left = i * 2
    right = left + 1
    largest = i

    if left < heapsize and vector[left].uid > vector[largest].uid:
        largest = left

    if right < heapsize and vector[right].uid > vector[largest].uid:
        largest = right

    if largest != i:
        swap(vector, i, largest)
        heapfy(vector, heapsize, largest)


def swap(vector, x, z):
    vector[x], vector[z] = vector[z], vector[x]
