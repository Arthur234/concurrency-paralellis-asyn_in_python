import threading
import time

from loguru import logger


from time_tracker import track_time


def target_function(thread_name):
    time.sleep(2)
    print(f"Run: {thread_name}")


def get_threads(threads_number=10):
    for i in range(threads_number):
        thread_name = f"Thread {i}"
        thread = threading.Thread(target=target_function, args=(thread_name,))
        yield thread


@track_time
def run_threads_without_order():
    logger.info("Run threads without order")
    threads = get_threads()
    for thread in threads:
        thread.start()
    logger.info("Main thread finished")


@track_time
def run_threads_with_order():
    logger.info("Run threads with order")
    threads = get_threads()
    for thread in threads:
        thread.start()
        thread.join()
    logger.info("Main thread finished")


if __name__ == '__main__':
    run_threads_without_order()
    run_threads_with_order()
