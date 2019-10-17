from argparse import ArgumentParser
from src import heap, selection


def arguments():
    args = ArgumentParser()
    args.add_argument("--a", type=str, help=" --a all, selection, insertion, merge, quicksort, heapsort or other",
                      required=True)
    args.add_argument("--input", type=str, help="--input data01.csv", required=False)
    args.add_argument("--out", type=str, help="--out data01_sorted.csv", required=False)
    return args.parse_args()


def select_run():
    args = arguments()
    algoritms = {
        "selection": selection.selection_sort,
        "insertion": "",
        "merge": "",
        "quick": "",
        "heap": heap.heap_sort
    }
    if args.input == "all":
        run_all()
    else:
        name = args.input.lower()
        selected = algoritms[name]
        run_script(selected)


def run_all():
    pass


def run_script(algoritm):
    pass
