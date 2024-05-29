# Exercise 3

## Scalability Analysis
The algorithm as implemented in `exercise1and2_losses_calculator.py` under `potential_financial_losses_estimate` experiences linear scaling, as demonstrated in ![image of scaling](takehome/benchmark.png) and through experimentation.

For a set of runs of varying size (n), we experience the following runtimes: 
n       |time(s)
---     |---
5       |1.2159347534179688e-05
10      |4.601478576660156e-05
100     |4.38690185546875e-05
1000    |0.0005209445953369141
10000   |0.00467681884765625
1000000 |0.53981614112854

The program is also linear in memory usage.

We note that running the proposed naieve solution on 1,000,000 buildsings in the given data format does not present a problem, but may be too time consuming for immediate user feedback.

## Optimization Strategies

1. Multiprocessing
The computations for each building are fully independent, meaning that they are "embarassingly parallel" and could be done all at the same time, rather than sequentially as our naieve implementation does.  One improvement for optimizing this code would be to evaluate buildings in parallel batches, with the size depending on the CPU in which the script is being run.  This can be done using a number of different frameworks, including asyncio, joblib, multiprocessing, etc...  In this paradigm, we can also manage the memory utilization by reading only once per batch, then controlling batch size to reduce the memory usage f required.

2. Vectorization
Another approach to improve the runtime here would be to vectorize the operations and instead use operations between arrays in numpy.  This in turn relies on lower-level C implementations of matrix operations, which tend to be far faster than python for-loops. One downside of this approach is it requires reading all data into memory at once.


## Resource Management

- monitor memory usage


## Example Code