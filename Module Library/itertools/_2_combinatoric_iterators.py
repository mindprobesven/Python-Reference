#!/usr/bin/env python3

# ----------------------------------------------------------------------------------------------------------------
# Module - itertools
#
# Combinatoric iterators
# The recursive generators that are used to simplify combinatorial constructs such as permutations, combinations, 
# and Cartesian products are called combinatoric iterators. In Python there are 4 combinatoric iterators:
#
# - Product
# - Permutations
# - Combinations
# ----------------------------------------------------------------------------------------------------------------

import itertools

if __name__ == '__main__':
    # Product()
    # This tool computes the cartesian product (A Cartesian Product is defined on an ordered set of sets. It is the 
    # set of all possible ordered combinations consisting of one member from each of those sets.of input iterables. 
    # To compute the product of an iterable with itself, we use the optional repeat keyword argument to specify the 
    # number of repetitions. The output of this function is tuples in sorted order.
    print("The cartesian product using repeat:")
    print(list(itertools.product([1, 2], repeat = 2)))
    print()
    
    print("The cartesian product of the containers:")
    print(list(itertools.product(['geeks', 'for', 'geeks'], '2')))
    print()
    
    print("The cartesian product of the containers:")
    print(list(itertools.product('AB', [3, 4])))

    # Permutations() 
    # Permutations() as the name speaks for itself is used to generate all possible permutations of an iterable. 
    # All elements are treated as unique based on their "position" and not their values. This function takes an 
    # iterable and group_size, if the value of group_size is not specified or is equal to None then the value of 
    # group_size becomes the length of the iterable.
    print (list(itertools.permutations('ABC')))     # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
    print()

    # Combinations()
    # This iterator prints all the possible combinations (without replacement) of the container passed in arguments 
    # in the specified "group size" in sorted order.
    print(list(itertools.combinations([1, 2, 3, 4], 2)))    # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    print()