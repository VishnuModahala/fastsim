import sum_metrics
import sys
#import numpy as np
import random

print("How big should the test array be?")
data_read = sys.stdin.readline()
scale = int(data_read)

test_array = [random.randint(0, 50) for i in range(scale)]

python_metrics = sum_metrics.python_sum_performance(test_array)
c_metrics = sum_metrics.c_sum_performance(test_array)
# numpy_metrics = sum_metrics.numpy_sum_performance(test_array)

print(f"{'Implementation':<20}{'Sum':>15}{'Time (s)':>15}{'Speedup':>12}")
print("-" * 65)

print(f"{'Python':<20}{python_metrics[0]:>15}{python_metrics[1]:>15.8f}{1.0:>12.2f}")
print(f"{'C':<20}{c_metrics[0]:>15}{c_metrics[1]:>15.8f}{(python_metrics[1]/c_metrics[1]):>12.2f}")
# print(f"{'NumPy':<20}{numpy_metrics[0]:>15}{numpy_metrics[1]:>15.5f}{python_metrics[1]/numpy_metrics[1]:>12.2f}")