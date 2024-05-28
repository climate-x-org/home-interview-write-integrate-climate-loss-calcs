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

## Optimization Strategies

## Resource Management

## Example Code