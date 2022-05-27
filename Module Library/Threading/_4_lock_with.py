#!/usr/bin/env python3

# ----------------------------------------------------------------------------------------------------------------
# Threading - Lock
#
# In this example, two threads (0 and 1) update a fake database value. A thread reads the value from the fake
# database, performs a caluclation and then updates the value in the database. This update takes two seconds,
# simulated with time.sleep(). When thread 0 performs the update and reaches time.sleep(), thread 1 will start
# and still get the old value from the database because thread 0 did not finish yet. A race condition occurs.
#
# A Lock is a way to avoid or solve race conditions. Only one thread at a time can have the Lock. Any other thread
# that wants the Lock must wait until the owner of the Lock gives it up. The basic functions to do this are
# .acquire() and .release(). Python’s Lock will also operate as a context manager, so you can use it in a with
# statement, and it gets released automatically when the with block exits for any reason.
# ----------------------------------------------------------------------------------------------------------------

import threading
import logging
import time
import concurrent.futures

class FakeDatabase:
    def __init__(self):
        # The fake database value
        self.value = 0
        self._lock = threading.Lock()

    # This method will cause a race condition
    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        # When thread 0 reaches sleep, thread 1 starts and will still read value = 0 because
        # thread 0 has not finished yet updating the database value after the sleep.
        time.sleep(2.0)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)

    # This method solves the race condition by using Lock()
    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        
        # Thread 0 acquires the lock and is still holding it when it goes to sleep.
        # Thread 1 then starts and attempts to acquire the same lock. Because Thread 0
        # is still holding it, Thread 1 has to wait. This is the mutual exclusion that
        # a Lock provides.
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(2.0)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)

    database = FakeDatabase()

    logging.info("Testing update. Starting value is %d.", database.value)

    # Thread 0 and 1 are created
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    
    logging.info("Testing update. Ending value is %d.", database.value)

    print("-" * 50)

    # The database value is reset to 0
    database.value = 0

    logging.info("Testing locked_update. Starting value is %d.", database.value)

    # Thread 0 and 1 are created
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    
    logging.info("Testing locked_update. Ending value is %d.", database.value)