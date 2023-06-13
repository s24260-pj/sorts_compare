import numpy as numpy
from time import perf_counter

from sort.heap_sort import heapsort
from sort.quick_sort import quicksort
from sort.selection_sort import selection_sort

array = numpy.random.randint(1, 1_000_000, 30_000)
array_3_unsorted = array.copy()
quicksort(array_3_unsorted, 0, len(array_3_unsorted) - 1)

array_sorted = numpy.flipud(array_3_unsorted)

arr_sorted_1 = array_sorted.copy()
arr_sorted_2 = array_sorted.copy()
arr_sorted_3 = array_sorted.copy()

start_time_heap = perf_counter()
heapsort(arr_sorted_2)
end_time_heap = perf_counter()

execution_time_heap = end_time_heap - start_time_heap
print("Czas wykonania heap sort: ", execution_time_heap, "s")

start_time_quick = perf_counter()
quicksort(arr_sorted_3, 0, len(arr_sorted_3) - 1)
end_time_quick = perf_counter()

execution_time_quick = end_time_quick - start_time_quick
print("Czas wykonania quick sort: ", execution_time_quick, "s")

start_time_selection = perf_counter()
selection_sort(arr_sorted_1)
end_time_selection = perf_counter()

execution_time_selection = end_time_selection - start_time_selection
print("Czas wykonania selection sort: ", execution_time_selection, "s")
