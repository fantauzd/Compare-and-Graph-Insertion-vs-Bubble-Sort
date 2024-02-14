# Author:  Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 11/22/2023
# Description: Compares the time it takes for the insertion sort and bubble sort functions to run on 10 lists of
#               different lengths. Creates a graph displaying the time per list length of both bubble and insertion
#               sort.

import time
import random
from matplotlib import pyplot
import functools


def sort_timer(func):
    """
    Uses the time module to record how many seconds a passed function takes to run. Then returns the run-time.
    :return: Time the decorated function took to run, in seconds.
    """

    @functools.wraps(func)  # use functools to keep docstrings accessible
    def wrapper(a_list):
        start = time.perf_counter()
        func(a_list)
        end = time.perf_counter()
        elapsed = end - start  # find how long the function took to run in seconds
        return elapsed

    return wrapper


@sort_timer
def bubble_sort(a_list):
    """
  Sorts a_list in ascending order using bubble sort.
  """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """
  Sorts a_list in ascending order using insertion sort.
  Should be faster than bubble sort.
  """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def make_lists_of_sort_times(first_sort, second_sort, list_of_lengths):
    """ Takes, as parameters, two sort functions and a list of lengths. The function then generates a random
    list of integers in [1,10000], equal in length to the first value in list_of_lengths.
    The function copies the random list of integers and passes it to both sort functions, getting the time each function
    took to complete the sort as a return. Saves the times each function took in separate lists. Once the time for each
    length has been found, the function places both lists (one for first_sort and one for second_sort) in a tuple and
    returns it.
    :return: a tuple of two lists, each containing the sort times for one of the functions
    ([first_sort],[second_sort])
    """
    first_sort_times = []  # initialize variables to store times for each sort
    second_sort_times = []
    # if list of lengths is longer than 10 then the return lists also be longer than 10
    for length in list_of_lengths:
        random_list_1 = []  # resets random list every time we run a new length from list_of_lengths

        for num in range(length):
            random_num = random.randint(1, 10000)
            random_list_1.append(random_num)  # adds "length" integers to random_list

        random_list_2 = list(random_list_1)  # makes a copy of our random list, so we can give one to each sort

        # the decorator function returns the time for each sort, which we append to our respective times list
        first_sort_times.append(first_sort(random_list_1))
        second_sort_times.append(second_sort(random_list_2))

    return (first_sort_times, second_sort_times)  # return lists in a tuple


def compare_sorts(first_sort, second_sort):
    """
    Takes two sort functions and creates a list of 10 lengths starting at 1000, in increments of 1000.
    Then passes the functions and lists to a function that returns a tuple of two lists, each containing the
    sort times for one of the functions ([first_sort],[second_sort]). Using this tuple, creates a graph comparing
    the time it takes each sort function to complete.
    :param first_sort: Bubble Sort
    :param second_sort: Insertion Sort
    :return: None. Displays a graph comparing sort times
    """
    # generates the list of lengths and then calls make_lists_of_sort_times()
    list_of_lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    tuple_of_times = make_lists_of_sort_times(first_sort, second_sort, list_of_lengths)
    # creates graph using our list of lenths and times
    pyplot.plot(list_of_lengths, tuple_of_times[0], 'ro--', linewidth=2, label='Bubble Sort')
    pyplot.plot(list_of_lengths, tuple_of_times[1], 'go--', linewidth=2, label='Insertion Sort')
    pyplot.xlabel("Size of List Being Sorted")
    pyplot.ylabel("Seconds to Sort")
    pyplot.legend(loc='upper left')
    pyplot.show()
    return

# main function included per assignment instruction
if __name__ == '__main__':
    compare_sorts(bubble_sort, insertion_sort)
