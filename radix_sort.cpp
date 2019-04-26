// C++11 implementation of Radix Sort 
#include <iostream>
#include <algorithm>
#include <fstream>
#include <iterator>
#include <vector>
#include <chrono>

using namespace std; 
using Clock = chrono::steady_clock;
using chrono::time_point;
// There are other clocks, but this is usually the one you want.
// It corresponds to CLOCK_MONOTONIC at the syscall level.
using chrono::duration_cast;
using chrono::milliseconds;


const char* INPUT_FILE = "million_ints.txt";
const int ITERATIONS = 10;
const int RADIX = 10;


// A utility function to get maximum value in arr[] 
int getMax(int arr[], int n) { 
	int mx = arr[0]; 
	for (int i = 1; i < n; i++) 
		if (arr[i] > mx) 
			mx = arr[i]; 
	return mx; 
} 

// A function to do counting sort of arr[] according to 
// the digit represented by exp. 
void countingSort(int arr[], int n, int exp) { 
	int output[n]; // output array 
	int i, count[RADIX] = {0}; 

	// Store count of occurrences in count[] 
	for (i = 0; i < n; i++) 
		count[(arr[i] / exp) % RADIX]++;

	// Change count[i] so that count[i] now contains actual 
	// position of this digit in output[] 
	for (i = 1; i < RADIX; i++) 
		count[i] += count[i - 1]; 

	// Build the output array 
	for (i = n - 1; i >= 0; i--) 
	{ 
		output[count[(arr[i] / exp) % RADIX] - 1] = arr[i]; 
		count[(arr[i] / exp) % RADIX]--; 
	} 

	// Copy the output array to arr[], so that arr[] now 
	// contains sorted numbers according to current digit 
	for (i = 0; i < n; i++) 
		arr[i] = output[i]; 
} 

// The main function to that sorts arr[] of size n using Radix Sort.
void radixsort(int arr[], int n) { 
	// Find the maximum number to know number of digits 
	int m = getMax(arr, n); 

	// Do counting sort for every digit. Note that instead 
	// of passing digit number, exp is passed. exp is 10^i 
	// where i is current digit number 
	for (int exp = 1; m/exp > 0; exp *= RADIX) 
		countingSort(arr, n, exp); 
} 

// Print an array of integers.
void print(int arr[], int n) 
{ 
	for (int i = 0; i < n; i++) 
		cout << arr[i] << " "; 
    cout << endl;
} 

// Populate an array with numbers from an input file.
int populatearrFromFile(const char* path, vector<int>& arr) {
    
    ifstream infile(path);

    if (infile.is_open() && infile.good()) {
        copy(istream_iterator<int>(infile), istream_iterator<int>(), back_inserter(arr));
        infile.close();
        return 0;
    } else {
        cout << "ERROR: Cannot read input file: " << path << endl;
        exit(1);
    }
    
}

int main(int argc, char **argv) {
    if (argc != 2) {
        cerr << "ERROR: Missing argument(s)." << endl;
        cerr << "usage: " << argv[0] << " <input_file>" << endl;
        exit(1);
    }

    const char* inputFile = argv[1];

    vector<int> arr;
    time_point<Clock> start, end;
    milliseconds elapsedTime;
    vector<milliseconds> runTimes;
    int totalTime, averageTime;

    start = Clock::now();
    populatearrFromFile(inputFile, arr);
    end = Clock::now();
    elapsedTime = duration_cast<milliseconds>(end - start);
    cout << "Import time: " << elapsedTime.count() << "ms" << endl;

    
    // Run and time radix sort.
    for (int i=0; i<ITERATIONS; i++) {
        // Randomize the order of the input array.
        random_shuffle(&arr[0], &arr[arr.size()]);
        
        start = Clock::now();
	    radixsort(&arr[0], arr.size()); 
        end = Clock::now();
        elapsedTime = duration_cast<milliseconds>(end - start);
        runTimes.push_back(elapsedTime);
        cout << "Iteration " << i << ": " << elapsedTime.count() << "ms" << endl;
    }

    // print(&arr[0], arr.size());
    totalTime = 0;
    for (auto& n : runTimes)
        totalTime += n.count();

    averageTime = totalTime / ITERATIONS;
    cout << "Average sort time: " << averageTime << "ms" << endl;

	return 0; 
}

