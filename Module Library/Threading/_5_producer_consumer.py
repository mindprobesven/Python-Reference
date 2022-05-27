#!/usr/bin/env python3

# ----------------------------------------------------------------------------------------------------------------
# Threading - Producer / Consumer using Lock
#
# This example demonstrates the inner workings of Lock()'s .acquire() and .release() functions.
# ----------------------------------------------------------------------------------------------------------------

import logging
import threading
import concurrent.futures
import random
import time

SENTINEL = object()

# A producer thread that reads from the fake network and puts the message into a Pipeline
def producer(pipeline):
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        # 2. The producer gets a burst of 10 messages and sends them to the pipeline ony by one
        pipeline.set_message(message, "Producer")
    # Send a sentinel message to tell consumer we're done
    pipeline.set_message(SENTINEL, "Producer")

# A consumer thread gets the message from the Pipeline and stores it in a fake database
def consumer(pipeline):
    """Pretend we're saving a number in the database."""
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            time.sleep(2.0)
            logging.info("Consumer storing message: %s", message)

# The Pipeline that passes messages from the producer to the consumer
class Pipeline:
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        # 1. The consumer thread is locked first. The consumer needs to wait until the first message is present.
        self.consumer_lock.acquire()

    def get_message(self, name):
        # 6. The consumer thread is locked again after receiving the first message.
        # 9. The consumer thread is locked again to wait for the next message to be present.
        logging.debug("%s:about to acquire getlock", name)
        self.consumer_lock.acquire()
        logging.debug("%s:have getlock", name)
        message = self.message
        # 7. The producer thread is released to set the second message
        logging.debug("%s:about to release setlock", name)
        self.producer_lock.release()
        logging.debug("%s:setlock released", name)
        # 8. The first message is returned and stored
        return message

    def set_message(self, message, name):
        # 3. The producer thread is locked, then sets self.message the first time.
        # 5. The producer thread gets the second message, but has to wait until the first message is stored by the consumer.
        # 10. The producer thread locks again and sets the second message.
        logging.debug("%s:about to acquire setlock", name)
        self.producer_lock.acquire()
        logging.debug("%s:have setlock", name)
        self.message = message
        # 4. The consumer thread lock is released because the first message is ready
        # 11. The consumer thread is released to store the second message
        logging.debug("%s:about to release getlock", name)
        self.consumer_lock.release()
        logging.debug("%s:getlock released", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
