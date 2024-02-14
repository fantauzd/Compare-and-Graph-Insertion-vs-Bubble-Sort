# project-8b

This may look intimidating at first glance, but if you just follow the steps, you'll be fine :)

For this project, you will import the **time** and **random** modules.  You will also install the **matplotlib** package and import from it the **pyplot** module.  You will also import the wraps() function from the functools module for use in your decorator

* Use the **time** module to write a decorator function named **sort_timer** that times how many seconds it takes the decorated function to run.  Since sort functions don't need to return anything, have the decorator's wrapper function return that elapsed time
  * To get the current time, call time.perf_counter().  Subtracting the begin time from the end time will give you the elapsed time in seconds

* Copy the code for bubble sort and insertion sort from Module 4 and decorate them with sort_timer. The names of the functions must be **bubble_sort** and **insertion_sort**.

* Write a function called **make_lists_of_sort_times** that takes three parameters: two sort functions and a list of lengths (which are ints). It will return (as a tuple) two lists of times, one for each sort algorithm
  * First it should randomly generate a list of n numbers, where n is the first value in the third parameter's list of lengths
  * The random numbers should all be integers in the range 1 <= r <= 10000
  * To generate random numbers, you will need to import the **random** module.  The function call random.randint(a, b) returns a random integer N such that a <= N <= b.  You should use a = 1 and b = 10000.  It's fine if values appear in the list multiple times
  * Then the function should make a separate copy of your list of random numbers, which you can do like this: list_2 = list(list_1)
  * Making a separate copy of the list is necessary because if you call a sort function on the list to record how long it takes, the list will now be sorted, which would affect how long the other sort function takes
  * Next the function should time how long it takes the first sort function to sort one copy of the list (using the first parameter), and then time how long it takes the second sort function to sort the other copy of the list (using the second parameter) This gets us the first data point for each algorithm's list of times
  * The function should now repeat these steps for each of the remaining values in the third parameter's list of lengths.  For each list size, the function should randomly generate a list of that size and time how long it takes each algorithm to sort it
  * Once the function has completed a list of the 10 time data points for each algorithm, it should return a tuple of the two lists - **first the list of sort times for the first sort function, then the list of sort times for the second sort function**
  * (Keep in mind that the time it takes an algorithm to sort a list depends on the list. Some algorithms will sort some lists faster than others. If you wanted your graph to be more robust, you would generate say 100 different random lists of each length and average their sort times together to get each data point.  However, that would take significantly longer to run, and therefore for the TAs to grade, so for this assignment, stick to one list of each size)

* Write a function called **compare_sorts** that takes the two decorated sort functions as parameters. It should call the make_lists_of_sort_times() function to get the tuple of the two lists of times, and then generate a graph comparing the times for each sort algorithm
  * The list it should pass to make_lists_of_sort_times() is [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
  * HINT: because sorting all those lists can take a while, you might want to start with something smaller for your initial debugging, like [100, 200, 300, 400, 500]
  * To generate a graph, you will need to install the **matplotlib** package and import **pyplot** from it.  Below is an example of code to produce a graph comparing two series of data points - **you will need to modify it to graph your timing data**

```
  from matplotlib import pyplot
  pyplot.plot([1, 2, 3, 4, 10], [1, 4, 9, 16, 100], 'ro--', linewidth=2, label='series 1')
  pyplot.plot([1, 2, 3, 4, 10], [1, 3, 7, 20, 150], 'go--', linewidth=2, label='series 2')
  pyplot.xlabel("the x label")
  pyplot.ylabel("the y label")
  pyplot.legend(loc='upper left')
  pyplot.show()
```
* Breakdown of graph example:
  * Each of the calls to the plot function plots a line
  * The call to the show function displays the graph
  * In the calls to the plot function, the first list is the list of x-coordinates (the lengths, which are the same for both curves you're plotting).  The second list is the list of y-coordinates (the list of times for a particular algorithm)
  * The 'ro--' tells it to use red circles connected by a dashed line and 'go--' is the same except green instead of red
  * The linewidth parameter is self-explanatory
  * The label parameter assigns the label to be used for that line in the legend. The legend() function sets where on the graph the legend should be displayed
  * The xlabel() and ylabel() functions set the labels for the x and y axes. For your graph, the x axis is the number of elements being sorted, and the y axis is the time in seconds
  * **Your graph must include a legend and labels for the axes.**

* You'll still submit this project in Gradescope. The autograder will make some checks that certain basic aspects of your sort times make sense. Since the TAs will need to run your code to check the graph, please include a main() function with the following line of code to call your compare_sorts() function to generate the graph:
```
compare_sorts(bubble_sort, insertion_sort)
```

Your graph should look similar to this:

![sort graph example](sort_graph_example.png)

Your file must be named: **sort_timer.py**
