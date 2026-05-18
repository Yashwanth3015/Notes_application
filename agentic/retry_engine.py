import time

from utils.logger import logger


class RetryEngine:

    @staticmethod
    def execute(function, retries=2, delay=2):

        last_exception = None   #used to remember final failure

        for attempt in range(retries + 1):

            try:
                return function()   #attempts to execute the function and returns result if successful

            except Exception as e:

                last_exception = e   #stores the exception for later use if all retries fail

                logger.warning(
                    f"Retry attempt {attempt + 1} failed"
                )

                time.sleep(delay)

        raise last_exception