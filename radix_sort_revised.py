#!/usr/bin/env python3
"""Python program for implementation of Radix Sort."""
import sys
import random
from timeit import default_timer as timer


OUTPUT_FILE = 'sorted_ints.txt'
ITERATIONS = 10
RADIX = 10


def counting_sort(arr, exp):
    rv = [0] * len(arr)
    count = [0] * RADIX

    for i in range(len(arr)):
        digit = (arr[i] // exp) % RADIX
        count[digit] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        digit = (arr[i] // exp) % RADIX
        rv[count[digit] - 1] = arr[i]
        count[digit] -= 1

    return rv


def radix_sort(arr): 
    """Perform radix sort on a list of ints."""
    max_val = max(arr)

    exp = 1
    while max_val // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= RADIX

    return arr


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('ERROR: Missing argument(s).')
        print('usage: {} <input_file>'.format(sys.argv[0]))
        sys.exit(1)

    input_file = sys.argv[1]

    start = timer()
    # Read ints from a file.
    try:
        with open(input_file, 'r') as fp:
            arr = [int(x) for x in fp.read().split()]
    except OSError:
        print("ERROR: Cannot read input file: {}".format(input_file))
        sys.exit(1)
    end = timer()
    elapsed_time = 1000 * (end - start)
    print('Import time: {}ms'.format(int(elapsed_time)))

    run_times = []

    # Run the sort 10 times, measuring the elapsed time for each iteration.
    for i in range(ITERATIONS):
        # Randomize the order of the input array.
        random.shuffle(arr)

        start = timer()
        arr = radix_sort(arr)
        end = timer()
        # Convert to milliseconds.
        elapsed_time = 1000 * (end - start)
        run_times.append(elapsed_time)
        print('Iteration {}: {}ms'.format(i + 1, int(elapsed_time)))
    
    average_time = sum(run_times) / ITERATIONS
    print('Average sort time: {}ms'.format(int(average_time)))

    # Write the results from the final sort to a file.
    # This will let us spot-check the output.
    try:
        with open(OUTPUT_FILE, 'w') as fp:
            fp.write(' '.join(str(x) for x in arr))
    except OSError:
        print("ERROR: Cannot write to output file: {}".format(OUTPUT_FILE))
        sys.exit(1)

