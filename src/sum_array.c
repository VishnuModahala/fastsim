#include <stdint.h>

int64_t sum_array(const int* inputArray, int length) {
    int64_t sum = 0;
    for (int i = 0; i < length; i++) {
        sum += inputArray[i];
    }
    return sum;
}