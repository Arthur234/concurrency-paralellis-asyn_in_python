import functools
from datetime import datetime

from loguru import logger


def track_time(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)

        execution_time = datetime.now() - start_time
        logger.info(f"Execution time: {execution_time}")
    return wrapper

