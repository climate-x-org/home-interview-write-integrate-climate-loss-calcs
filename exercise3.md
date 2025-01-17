# Exercise 3:

## Complexity
The complexity of the current system is linear to the number of buildings provided.
I have added tracking of the execution time to both scripts.
I then created a utility that facilitates the creation of very large JSON files with random data.

This allowed me to proove that the execution time grows linearly, compared to the size of the data set.

Exercise 2 takes about 2 seconds to run, for 1M buildings.
This means that it would take around 200 seconds to run for 200M buildings, assuming that there would be enough memory to load all the data. 

This could be ok for something that needs to run in the background, but it would probably be too long if it needs to provide real time feedback to a user interface.

One possible approach for improving performance would be to parallelize the execution.
To test this I have modified the script so that the datato be output would first be saved into an array, and then displayed on screen.
I was then able to process the array in chuncks, in parallel and then output the data on screen.

Although the mathematical calculations used are not extremely complex and take a very short time to run, I was able to have some performance gain.
If we only consider the time it takes to run the calculations and fill the array with the data be displayed, I was able to shorten the execution time from 500ms to 400ms using chunks of 20.000 items.
In a rea-lworld application that uses a more complex and time consuming logic, the performance gain should be more  noticeable.

More sophisticated approaches vould involve first of all a better data storage solution.
Storing the data in a relational database like Postgres would allow us to process the data in chunks using a queuing system, that is also able to execute many jobs in parallel.
In this scenario, increasing the processing speed would become a matter of assigning more resources to the queuing system so that a lot of jobs can be processed in parallel.

We would then face the challenge of knowing when all of the data has been processed.
Each job would only know when its single chunk has all been processed, but there would not be anything in place that knows when all of the chunks have been processed.
One solution to this challenge could be to lazy-load the data.
Essentially,  the interface would only load the data as it becomes available so that we do not need to know if all of the data has been processed.

