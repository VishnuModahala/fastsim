#include <stdint.h>

long sum_array(const int* inputArray, int length) {
    long sum = 0;
    for (int i = 0; i < length; i++) {
        sum += inputArray[i];
    }
    return sum;
}