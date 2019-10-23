import timeout


@timeout.timeout(900)
def run(V):
    merge_sort(V)


def merge_sort(V):
    if len(V) > 1:
        mid = len(V) // 2
        L = V[:mid]
        R = V[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(V, L, R)


def merge(V, L, R):
    i = 0
    j = 0
    k = 0
    l_L = len(L)
    l_R = len(R)

    while i < l_L and j < l_R:
        if L[i].uid < (R[j]).uid:
            V[k] = L[i]
            i += 1
        else:
            V[k] = R[j]
            j += 1
        k += 1

    while i < l_L:
        V[k] = L[i]
        i += 1
        k += 1
    while j < l_R:
        V[k] = R[j]
        j += 1
        k += 1
