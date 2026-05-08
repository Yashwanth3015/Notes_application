class FailureAnalyzer:

    @staticmethod
    def analyze(exception):

        message = str(exception)

        if "TimeoutException" in message:
            return "Synchronization Failure"

        if "NoSuchElementException" in message:
            return "Locator Failure"

        return "Unknown Failure"