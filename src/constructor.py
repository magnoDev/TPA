from argparse import ArgumentParser
import time, heap, selection, data_manager, signal

_ALGORITHMS_list = ["selection", "insertion", "merge", "quick", "heap"]
_ALGORITHMS_dict = {
    "selection": selection.run,
    "insertion": heap.run,
    "merge": heap.run,
    "quick": heap.run,
    "heap": heap.run
}


def arguments():
    args = ArgumentParser()
    args.add_argument("--a", type=str, help=" --a all, selection, insertion, merge, quick, heap or other",
                      required=True)
    args.add_argument("--input", type=str, help="--input data01.csv", required=False)
    args.add_argument("--output", type=str, help="--output data01_sorted.csv", required=False)
    args.add_argument("--times", type=str, help="--times 10", required=False)
    return args.parse_args()


def run():
    args = arguments()

    if args.a == "all":

        run_all(args.input, args.output)
    else:
        selected = _ALGORITHMS_dict[args.a]
        run_sort(selected, args.input, args.output, args.a, int(args.times))


def run_all(input, output, times=1):
    times = 1 if times == None else times
    files = data_manager.list_files()
    for a in _ALGORITHMS_list:
        for f in files:
            algorithm = _ALGORITHMS_dict[a]
            run_sort(algorithm, f, f, a, times)


def run_sort(algorithm, input, output, alg_name, times):
    timeout = 900  # standard 15 minutes
    i_time = 0
    f_time = 0
    max_time = 0
    min_time = 3600
    med_time = 0
    isTimeout = False
    records = []
    # signal.signal(signal.SIGALRM, handler)  # only linux
    times = 1 if times == None else times
    if not isTimeout:
        for i in range(times):
            data = data_manager.open_input_file(input)
            try:
                i_time = time.time()
                # signal.alarm(timeout)
                algorithm(data)
                # signal.alarm(0)
                f_time = time.time()
            except:
                isTimeout = True
            dif_time = f_time - i_time
            med_time += dif_time
            if dif_time < min_time:
                min_time = dif_time
            if dif_time > max_time:
                max_time = dif_time
            data_manager.save_file("%s_%d_%s" % (alg_name, i + 1, output), data)
            print("Terminou: %d/%d tempo: %f" % (i + 1, times, dif_time))
        print("max: %f min: %f med: %f" % (max_time, min_time, (med_time / times)))
        records.append([alg_name, times, min_time, max_time, (med_time / times)])

    else:
        print("timeout")
    data_manager.save_record_time(records)


def handler(signum, frame):
    raise Exception("end of time")
