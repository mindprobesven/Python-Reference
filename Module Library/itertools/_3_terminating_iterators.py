#!/usr/bin/env python3

# ----------------------------------------------------------------------------------------------------------------
# Module - itertools
#
# Terinating iterators
# Terminating iterators are used to work on short input sequences and produce the output based on the 
# functionality of the method used.
# ----------------------------------------------------------------------------------------------------------------

import itertools
import operator

if __name__ == '__main__':
    # accumulate(iter, func)
    # This iterator takes two arguments, iterable target and the function which would be followed at each 
    # iteration of value in target. If no function is passed, "addition" takes place by default. If the input iterable 
    # is empty, the output iterable will also be empty.
    number_list = [1, 4, 5, 7]

    # Prints the successive summation of elements
    print ("The sum after each iteration is : ", end ="")
    print (list(itertools.accumulate(number_list))) # The sum after each iteration is : [1, 5, 10, 17]

    # Prints the successive multiplication of elements, using operator.mul
    print ("The product after each iteration is : ", end ="")
    print (list(itertools.accumulate(number_list, operator.mul)))   # The product after each iteration is : [1, 4, 20, 140]

    # chain(iter1, iter2..)
    # This function is used to print all the values in iterable targets one after another mentioned in its arguments.
    li1 = [1, 4, 5, 7]
    li2 = [1, 6, 5, 9]
    li3 = [8, 10, 5, 4]
    
    print ("All values in mentioned chain are : ", end ="")
    print (list(itertools.chain(li1, li2, li3)))    # [1, 4, 5, 7, 1, 6, 5, 9, 8, 10, 5, 4]

    # chain.from_iterable()
    # This function is implemented similarly as a chain() but the argument here is a list of lists or any other 
    # iterable container.
    list_of_lists = [li1, li2, li3]

    print ("All values in mentioned chain are : ", end ="")
    print (list(itertools.chain.from_iterable(list_of_lists)))   # [1, 4, 5, 7, 1, 6, 5, 9, 8, 10, 5, 4]

    # filterfalse(func, seq) 
    # As the name suggests, this iterator prints only values that return false for the passed function.
    li = [2, 4, 5, 7, 8]
    
    print ("The values that return false to function are : ", end ="")
    print (list(itertools.filterfalse(lambda x : x % 2 == 0, li)))  # [5, 7]

    # islice(iterable, start, stop, step)
    # This iterator selectively prints the values mentioned in its iterable container passed as argument. This 
    # iterator takes 4 arguments, iterable container, starting pos., ending position and step.
    li = [2, 4, 5, 7, 8, 10, 20]

    # starts printing from 2nd index till 6th skipping 2
    print ("The sliced list values are : ", end ="")
    print (list(itertools.islice(li, 1, 6, 2))) # [4, 7, 10]

    # starmap(func., tuple list)
    # This iterator takes a function and tuple list as argument and returns the value according to the function 
    # from each tuple of the list.
    li = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1) ]
   
    # selects min of all tuple values
    print ("The values acc. to function are : ", end ="")
    print (list(itertools.starmap(min, li)))    # [1, 1, 4, 1]

    # takewhile(func, iterable)
    # This iterator prints the values till the function returns false for 1st time.
    li = [2, 4, 6, 7, 8, 10, 20]
   
    print ("The list values till 1st false value are : ", end ="")
    print (list(itertools.takewhile(lambda x : x % 2 == 0, li )))   # [2, 4, 6]