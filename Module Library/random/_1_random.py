#!/usr/bin/env python3

# ----------------------------------------------------------------------------------------------------------------
# Module - random
#
# In-built module of Python which is used to generate random numbers. These are pseudo-random numbers means these 
# are not truly random. This module can be used to perform random actions such as generating random numbers, print 
# random a value for a list or string, etc.
# ----------------------------------------------------------------------------------------------------------------

import random

if __name__ == '__main__':
    # Specifying a seed
    random.seed(444)

    # random.choice(sequence)
    # Printing a random value from a list
    list1 = [1, 2, 3, 4, 5, 6]
    print(random.choice(list1)) # 3

    # random.randint(start, end)
    # Generate random integers between the given range
    r1 = random.randint(5, 15)
    print("Random number between 5 and 15 is % s" % (r1))   # Random number between 5 and 15 is 9

    #random.random()
    # Generate random floats between 0.0 to 1
    print(random.random())  # 0.01323751590501987

    # random.shuffle(sequence, function)
    # Shuffle a sequence (list). Shuffling means changing the position of the elements of the sequence.
    sample_list = [1, 2, 3, 4, 5]
    random.shuffle(sample_list)
    print(sample_list)  # [1, 5, 2, 3, 4]