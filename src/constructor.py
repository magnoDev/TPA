from argparse import ArgumentParser
import time, heap, selection, data_manager


def arguments():
    args = ArgumentParser()
    args.add_argument("--a", type=str, help=" --a all, selection, insertion, merge, quicksort, heapsort or other",
                      required=True)
    args.add_argument("--input", type=str, help="--input data01.csv", required=False)
    args.add_argument("--output", type=str, help="--output data01_sorted.csv", required=False)
    return args.parse_args()


def run():
    args = arguments()
    algorithms = {
        "selection": [selection.run],
        "insertion": [heap.run],
        "merge": [heap.run],
        "quick": [heap.run],
        "heap": [heap.run]
    }
    if args.a == "all":

        run_all(args.input, args.output)
    else:
        selected = algorithms[args.a][0]
        run_sort(selected, args.input, args.output)


def run_all(input, output, times=1):
    print("nada aqui")


def run_sort(algorithm, input, output, times=10):
    timeout = 900  # standard 15 minutes
    i_time = 0
    f_time = 0
    max_time = 0
    min_time = 3600
    med_time = 0
    for i in range(times):
        data = data_manager.open_input_file(input)
        i_time = time.time()
        algorithm(data)
        f_time = time.time()
        dif_time = f_time - i_time
        med_time += dif_time
        if dif_time < min_time:
            min_time = dif_time
        if dif_time > max_time:
            max_time = dif_time
        print("Terminou: %d tempo: %f" % ((times - i), dif_time))
    print("max: %f min: %f med: %f" % (max_time, min_time, (med_time / times)))
