from .htree import HeapTree
def heap_sort(vector):
    htree = HeapTree.heap_gen(vector)

def heapfy(vector, i):
    l , r, largest = 0
    r = right(i)


void HEAPIFY(int A[ ], int heapsize, int i){
    int l, r, largest;
l = left(i);
r = right(i);
if ((l <= heapsize) && (A[l] > A[i]))largest = l;
elselargest = i;
if ((r <= heapsize) && (A[r] > A[largest]))largest = r;
if (largest != i){swap(A[i], A[largest]);
/* troca a posicao dos elementos */
                       HEAPIFY(A, heapsize, largest);
return 0
}