def selection_sort(arr):
    arr_size = len(arr)

    for i in range(arr_size):
        min_idx = i
        for j in range(i + 1, arr_size):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
