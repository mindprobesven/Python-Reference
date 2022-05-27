#!/usr/bin/env python3

# ----------------------------------------------------------------------------------------------------------------
# Threading - Producer / Consumer using Queue (Simplified)
#
# In the previous example, pipeline is not really necessary and can become just queue.Queue() to simplify.
# ----------------------------------------------------------------------------------------------------------------

import logging
import threading
import concurrent.futures
import queue
import random
import time

def producer(queue, event):
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        queue.put(message)

    logging.info("Producer received event. Exiting")

def consumer(queue, event):
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(
            "Consumer storing message: %s (size=%d)", message, queue.qsize()
        )
        time.sleep(1.0)

    logging.info("Consumer received event. Exiting")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    # Instead of the pipeline, we simply use queue.Queue() directly
    queue = queue.Queue(maxsize=10)
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, queue, event)
        executor.submit(consumer, queue, event)

        time.sleep(3.0)
        logging.info("Main: about to set event")
        event.set()
