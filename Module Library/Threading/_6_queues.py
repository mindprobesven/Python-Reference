#!/usr/bin/env python3

# ----------------------------------------------------------------------------------------------------------------
# Threading - Producer / Consumer using Queue
#
# To be able to handle more than one value in the pipeline at a time, we need a data structure for the pipeline 
# that allows the number to grow and shrink as data backs up from the producer. Here we use a Queue instead of 
# just a variable protected by a Lock. We also use a different way to stop the worker threads by using a different
# primitive from Python threading, an Event.
# ----------------------------------------------------------------------------------------------------------------

import logging
import threading
import concurrent.futures
import queue
import random
import time

def producer(pipeline, event):
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    logging.info("Producer received EXIT event. Exiting")

def consumer(pipeline, event):
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info(
            "Consumer storing message: %s  (queue size=%s)",
            message,
            pipeline.qsize(),
        )
        time.sleep(1.0)

    logging.info("Consumer received EXIT event. Exiting")

# The pipeline is a subclass of Queue. Queue is frequently used in multi-threading
# environments and incorporated all of that locking code inside the Queue itself.
# Queue is thread-safe.
class Pipeline(queue.Queue):
    def __init__(self):
        # Here we specify the maximum size of the queue
        super().__init__(maxsize=10)

    def get_message(self, name):
        logging.debug("%s:about to get from queue", name)
        # Get an item from the queue
        value = self.get()
        logging.debug("%s:got %d from queue", name, value)
        return value

    def set_message(self, value, name):
        logging.debug("%s:about to add %d to queue", name, value)
        # Add an item to the queue
        self.put(value)
        logging.debug("%s:added %d to queue", name, value)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # The time.sleep(3.0) will let the producer get as many messages as it can in 3 seconds. It stops
        # when the queue is full (set to 10) and then waits until the queue frees up to get more messages.
        # It exits when event.set() is executed after 3 seconds.
        executor.submit(producer, pipeline, event)

        # The consumer with time.sleep(1.0) requires one second to process a single message from the queue.
        executor.submit(consumer, pipeline, event)

        time.sleep(3.0)
        logging.info("Main: about to set event")
        event.set()