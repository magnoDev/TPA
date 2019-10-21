from argparse import ArgumentParser
import time, heap, selection, data_manager, quick, merge, insertionsort
import signal

_ALGORITHMS_list = ["selection", "insertion", "merge", "quick", "heap"]
_ALGORITHMS_dict = {
    "selection": selection.run,
    "insertion": insertionsort.run,
    "merge": merge.run,
    "quick": quick.run,
    "heap": heap.run
}
_TIMEOUT_dict = {
    "selection": 6,
    "insertion": 6,
    "merge": 6,
    "quick": 6,
    "heap": 6
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
    if args.times == None:
        args.times = 1
    if args.a == "all":

        run_all(args.input, args.output, int(args.times))
    else:
        selected = _ALGORITHMS_dict[args.a]

        run_sort(selected, args.input, args.output, args.a, int(args.times))


def run_all(input, output, times=1):
    times = 1 if times == None else times
    files = data_manager.list_files()
    for f in files:
        for a in _ALGORITHMS_list:
            algorithm = _ALGORITHMS_dict[a]
            run_sort(algorithm, f, f, a, times)


def run_sort(algorithm, input, output, alg_name, times):
    print("runsort: " + alg_name)
    timeout = 900  # standard 15 minutes
    i_time = 0
    f_time = 0
    max_time = 0
    min_time = 1800
    med_time = 0
    isTimeout = False
    records = []
    # signal.signal(signal.SIGALRM, handler)  # only linux
    times = 1 if times == None else times
    if int(input[-5]) > _TIMEOUT_dict[alg_name]:
        isTimeout = True
        print("pulou: %s tamanho: %s" % (alg_name, input[-5]))
    for i in range(times):
        print("run %d / %d" % (times - i, times))
        if not isTimeout:
            data = data_manager.open_input_file(input)
            try:
                i_time = time.time()

                # signal.alarm(timeout)
                algorithm(data)
                # signal.alarm(0)
                f_time = time.time()
            except Exception as err:
                print("Erro no Sort: %s" % (err))
                isTimeout = True
                _TIMEOUT_dict[alg_name] = int(input[-5])
                print("new Timeout %d" % _TIMEOUT_dict[alg_name])

            dif_time = f_time - i_time
            if min_time > dif_time:
                min_time = dif_time
            if max_time < dif_time:
                max_time = dif_time
            print("Terminou: %s(%s),  %d/%d tempo: %f" % (alg_name, input[5:-4], i + 1, times, dif_time))
    if not isTimeout:
        # data_manager.save_file("%s_%d_%s" % (alg_name, i + 1, output), data)
        print("max: %f min: %f med: %f" % (max_time, min_time, ((max_time + min_time) / 2)))
        records.append([alg_name, input[5:-4], min_time, max_time, ((max_time + min_time) / 2)])
    else:
        print("Not executed")
        records.append([alg_name, input[5:-4], -1, -1, -1])

    data_manager.save_record_time(records)
    print("records saved")


def handler(signum, frame):
    raise Exception("end of time")
