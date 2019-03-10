#!/usr/bin/env python3
# Modified from Manish Bhojasia's implmentation
# https://www.sanfoundry.com/python-program-implement-radix-sort/

import sys
import textwrap
import timeit

count = 10
range_size = 1000000

def radix_sort(int_array, base=10):
    def key_factory(digit, base):
        def key(int_array, index):
            return ((int_array[index]//(base**digit)) % base)
        return key
    largest = max(int_array)
    exp = 0
    while base**exp <= largest:
        int_array = counting_sort(int_array, base - 1, key_factory(exp, base))
        exp = exp + 1
    return int_array



def counting_sort(int_array, largest, key):
    c = [0]*(largest + 1)
    for i in range(len(int_array)):
        c[key(int_array, i)] = c[key(int_array, i)] + 1

    # Find the last index for each element
    c[0] = c[0] - 1 # to decrement each element for zero-based indexing
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None]*len(int_array)
    for i in range(len(int_array) - 1, -1, -1):
        result[c[key(int_array, i)]] = int_array[i]
        c[key(int_array, i)] = c[key(int_array, i)] - 1
    return result



def show_results(result):
    global count, range_size
    per_pass = (result / count)
    print('\n{:.6f} sec/pass'.format(per_pass), end=' ')
    per_item = per_pass / range_size
    print('\n{:.6f} sec/item\n'.format(per_item))



t1 = timeit.Timer(textwrap.dedent(
'''try:
    with open(sys.argv[1], 'r') as f:
        int_array = [int(x) for x in f.read().split()]
except IndexError:
    print("Usage: ./$filename.py $unsorted_input.txt")
    sys.exit(0)'''))
print('\n***** IMPORT TIMING RESULTS *****')
show_results(t1.timeit(number=count))

try:
    with open(sys.argv[1], 'r') as f:
        int_array = [int(x) for x in f.read().split()]
except IndexError:
    print("Usage: ./$filename.py $unsorted_input.txt")
    sys.exit(0)

t2 = timeit.Timer('radix_sort(int_array)', 'from __main__ import radix_sort, int_array')
print('\n***** SORT TIMING RESULTS *****')
show_results(t2.timeit(number=count))

#print('Sorted list: ', end='')
#print(sorted_list)
