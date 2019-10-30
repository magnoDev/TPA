import src.selection as sel
import src.quicksort as qk
import src.introsort as ins

def main():
    # vector = [5, 4, 3, 2, 1, 9, 8, 7, 6]
    # sel.selection(vector)
    # qk.quicksort(vector, 0, 8)
    # print(vector)

    arr = [2, 10, 24, 2, 10, 11, 27, 4, 2, 4, 28, 16, 9, 8,28, 10, 13, 24, 22, 28, 0, 13, 27, 13, 3, 23, 18, 22, 8, 8]
    #n = len(arr)

    ins.introsort(arr)
    print(arr)

if __name__ == '__main__':
    main()
