# radix-sort-comparison
*Usage: ./radix-sort-comparison.py $input_file*

Note that the purposes of timing, the file currently has the 'count' and 'range' variables set for 10^7 ints. This may be changed in the future to read inputs from sys.argv, as using an array size other than that included would throw off the calcs.

Code is modified from [Manish Bhojasia](https://www.sanfoundry.com/python-program-implement-radix-sort/)

The intent is to perform timing of a radix sort on various platforms, such as a GPU, a multiple-GPU AWS instance, a Raspberry Pi, laptop, etc.
