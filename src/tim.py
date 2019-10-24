import insertionsort, merge 

import timeout


@timeout.timeout(900)
def run(V):
    timSort(V)

def timSort(vector):  
    tam = len(vector)
    n = 32
    for i in range(0, tam, n):  
        insertionsort.run(vector[i:min((i+n-1), (n-1))])  
    size = n 
    while size < tam:   
        for L in range(0, tam, 2*size):  
            mid = L + size - 1 
            R = min((L + 2*size - 1), (n-1))  
            merge.merge(vector, L, R)  
        size = 2*size 