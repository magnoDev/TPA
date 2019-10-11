from src import heap, selection, data_manager


def main():
    files = data_manager.list_files()

    vector = data_manager.open_input_file(files[0])
    selection.selection_sort(vector)
    print(data_manager.is_sorted(vector))
    data_manager.save_file("teste.csv", vector)


if __name__ == '__main__':
    main()
