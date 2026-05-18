from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException
)

from agentic.execution_context import (
    ExecutionContext
)


class FailureAnalyzer:

    @staticmethod
    def analyze(exception):

        # -----------------------------------------
        # TIMEOUT
        # -----------------------------------------

        if isinstance(exception, TimeoutException):

            failure = (
                "Synchronization Failure"
            )

        # -----------------------------------------
        # LOCATOR FAILURE
        # -----------------------------------------

        elif isinstance(           #instance checks the object type
            exception,
            NoSuchElementException
        ):

            failure = (
                "Locator Failure"
            )

        # -----------------------------------------
        # CLICK INTERCEPTION
        # -----------------------------------------

        elif isinstance(
            exception,
            ElementClickInterceptedException
        ):

            failure = (
                "Click Interception"
            )

        else:

            failure = (
                "Unknown Failure"
            )

        ExecutionContext.failure_type = (
            failure
        )

        ExecutionContext.last_failure = (
            str(exception)
        )

        return failure