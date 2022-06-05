#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Module - time
# ----------------------------------------------------------------------------------------------------------------

import time

if __name__ == "__main__":
    # The time() function returns the number of seconds passed since epoch.
    # For Unix system, January 1, 1970, 00:00:00 at UTC is epoch
    print(time.time())      # 1654442171.067335

    # Convert a time expressed in seconds since the epoch to a string of a form: 'Sun Jun 20 23:21:05 1993' 
    # representing local time.
    # The time.ctime() function takes seconds passed since epoch as an argument
    print(time.ctime(10))   # Thu Jan  1 01:00:10 1970
    # If secs is not provided or None, the current time as returned
    print(time.ctime())   # Sun Jun  5 17:20:21 2022

    # Several functions in the time module such as gmtime(), asctime() etc. either take time.struct_time object 
    # as an argument or return it. Here's an example of time.struct_time object.
    # The type of the time value sequence returned by gmtime(), localtime(), and strptime(). It is an object with a named tuple 
    # interface: values can be accessed by index and by attribute name.
    #
    # time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27, tm_hour=6, tm_min=35, tm_sec=17, tm_wday=3, tm_yday=361, tm_isdst=0)

    # The localtime() function takes the number of seconds passed since epoch as an argument and returns a 
    # struct_time object in local time. If no argument or None is passed to localtime(), the value returned by time() is used.
    result = time.localtime(10)
    print(result)   # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=1, tm_min=0, tm_sec=10, tm_wday=3, tm_yday=1, tm_isdst=0)
    print(result.tm_year)   # 1970

    # The gmtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in UTC.
    result = time.gmtime(10)
    print(result)   # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=1, tm_min=0, tm_sec=10, tm_wday=3, tm_yday=1, tm_isdst=0)
    print(result.tm_year)   # 1970

    # The mktime() function takes struct_time (or a tuple containing 9 elements corresponding to struct_time) as an argument 
    # and returns the seconds passed since epoch in local time. Basically, it's the inverse function of localtime().
    t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
    local_time = time.mktime(t)
    print("Local time:", local_time)
    # Here we first create a struct_time object to pass to mktime()
    t = time.localtime(10)
    local_time = time.mktime(t)
    print("Local time:", local_time)

    # The asctime() function takes struct_time (or a tuple containing 9 elements corresponding to struct_time) as an argument and 
    # returns a string representing it.
    t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
    result = time.asctime(t)
    print("Result:", result)    # Result: Fri Dec 28 08:44:04 2018

    # The strftime() function takes struct_time (or tuple corresponding to it) as an argument and returns a string representing it based 
    # on the format code used.
    named_tuple = time.localtime() # get struct_time object
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    print(time_string)  # 06/05/2022, 17:43:22

    # The strptime() function parses a string representing time and returns struct_time object.
    time_string = "21 June, 2018"
    result = time.strptime(time_string, "%d %B, %Y")
    print(result) # time.struct_time(tm_year=2018, tm_mon=6, tm_mday=21, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=172, tm_isdst=-1)

    # The perf_counter() returns the value (in fractional seconds) of a performance counter
    start_time = time.perf_counter()
    print(start_time)
    time.sleep(1)
    end_time = time.perf_counter()
    print(end_time)
    print(f'Elapsed seconds: {end_time - start_time}')  # Elapsed seconds: 1.0011223460314795