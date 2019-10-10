def selection_sort(vector):
    for index in range(len(vector)):
        minor = index
        for next in range(index + 1, len(vector)):
            if vector[minor] > vector[next]:
                minor = next
        vector[index], vector[minor] = vector[minor], vector[index]
