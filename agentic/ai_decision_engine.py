class AIDecisionEngine:

    @staticmethod
    def should_retry(failure_type):

        retryable = [
            "Synchronization Failure",
            "Locator Failure"
        ]

        return failure_type in retryable