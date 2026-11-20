# import numpy as np
import ctypes
import time

lib = ctypes.CDLL("./libsum.so")

lib.sum_array.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
lib.sum_array.restype = ctypes.c_long


# Purely Python summing implementation
def python_sum_performance(arr):

    start = time.perf_counter()
    total = 0
    for i in arr:
        total += i
    python_time = time.perf_counter() - start

    results = [total, python_time]
    return results

def c_sum_performance(arr):

    length = len(arr)
    c_arr = (ctypes.c_int * length)(*arr)

    start = time.perf_counter()
    total = lib.sum_array(c_arr, length)
    c_time = time.perf_counter() - start
    
    results = [total, c_time]
    return results

# def numpy_sum_performance(arr):

#     start = time.perf_counter()
#     total = np.sum(arr)
#     numpy_time = time.perf_counter() - start
    
#     results = [total, numpy_time]
#     return results