#!/usr/bin/env python3

# ----------------------------------------------------------------------------------------------------------------
# Module - itertools
#
# Python’s Itertool is a module that provides various functions that work on iterators to produce complex iterators. 
# This module works as a fast, memory-efficient tool that is used either by themselves or in combination to form 
# iterator algebra.
#
# Different types of iterators provided by this module are: 
#
# - Infinite iterators
# - Combinatoric iterators
# - Terminating iterators
#
# Infinite iterators
# Iterator in Python is any Python type that can be used with a ‘for in loop’. Python lists, tuples, dictionaries, 
# and sets are all examples of inbuilt iterators. But it is not necessary that an iterator object has to exhaust, 
# sometimes it can be infinite. Such types of iterators are known as Infinite iterators.
# ----------------------------------------------------------------------------------------------------------------

import itertools

if __name__ == '__main__':
    # count(start, step)
    # This iterator starts printing from the “start” number and prints infinitely
    for i in itertools.count(5, 5):
        if i == 35:
            break
        else:
            print(i, end=" ")      # 5 10 15 20 25 30

    # cycle(iterable) 
    # This iterator prints all values in order from the passed container. It restarts printing from the beginning 
    # again when all elements are printed in a cyclic manner.
    count = 0
    for i in itertools.cycle('Sven'):
        if count > 20:
            break
        else:
            print(i, end=" ")   # S v e n S v e n S v e n S v e n S v e n S 
            count += 1

    # repeat(val, num) 
    # This iterator repeatedly prints the passed value an infinite number of times. If the optional keyword num is 
    # mentioned, then it repeatedly prints num number of times.
    print(list(itertools.repeat('Sven', 5)))    # ['Sven', 'Sven', 'Sven', 'Sven', 'Sven']