import timeout


@timeout.timeout(900)
def run(V):
    quicksort(V)


def quicksort(l):
    if l:
        left = [x for x in l if x.uid < l[0].uid]
        right = [x for x in l if x.uid > l[0].uid]
        if len(left) > 1:
            left = quicksort(left)
        if len(right) > 1:
            right = quicksort(right)
        return left + [l[0]] * l.count(l[0]) + right
