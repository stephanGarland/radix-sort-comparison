# Radix Sort
The purpose of this project is to run radix sort a standalone Nvidia GPU, multiple-GPU AWS instance, Raspberry Pi, Linux, macOS and Windows, and to then analyze the timing data cross the platforms.

## Python 3 Implementation
*Usage: ./radix_sort_revised.py <input_file>*

## C++11 Implementation
*Usage: ./radix_sort <input_file>*
To compile: `g++ -std=c++11 -o radix_sort radix_sort.cpp`

## CUDA Implementation
https://github.com/mark-poscablo/gpu-radix-sort

Compiling on:
- Windows 10 using nvcc

Running on:
- Nvidia GeForce GTX 1070
