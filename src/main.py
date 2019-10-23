import src.selection as sel
import src.quicksort as qk

def main():
    vector = [5, 4, 3, 2, 1, 9, 8, 7, 6]
    sel.selection(vector)
    qk.quicksort(vector, 0, 8)
    print(vector)

if __name__ == '__main__':
    main()
