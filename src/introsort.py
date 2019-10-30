import math
import src.heapsort as hs
import src.insertionSort as sl


# https://www.geeksforgeeks.org/quick-sort/

def partition(arr, low, high):
    # pivot

    pivot = arr[high]

    # index of smaller element

    i = low - 1

    for j in range(low, high):

        # If the current element is smaller than or
        # equal to the pivot

        if arr[j] <= pivot:
            # increment index of smaller element

            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


# https://www.geeksforgeeks.org/introsort-or-introspective-sort/

# def introSort(A, begin, end):
#     depth_limit = 2 * math.log2(end - begin)
#     n = len(A)
#
#     if n <= 16:
#         sl.insertionsort(A)
#
#     if depth_limit == 0:
#         hs.heap_sort(A)
#
#     else:
#         p = partition(A, begin, end)
#         introSort(A, A[0:p - 1], depth_limit - 1)
#         introSort(A, A[p + 1:n], depth_limit - 1)


def introsort(A):
    dephtLimit = 2 * math.log2(len(A))
    introsort_impl(A, dephtLimit)

def introsort_impl(A, depth_limit):
    #ao que parece o fim é sempre o len -1, tem que começar assim
    n = len(A)
    begin = A[0]
    end = len(A) - 1


    if n <= 16:
        sl.insertionsort(A)

    if depth_limit == 0:
        hs.heap_sort(A)

    else:
        p = partition(A, begin, end)
        #conferir corretude de acordo com a lógica
        introsort_impl(A[0:p - 1], depth_limit - 1)
        introsort_impl(A[p + 1:n], depth_limit - 1)
