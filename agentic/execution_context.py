#store runtime AI failure information during test execution for self-healing purposes
class ExecutionContext:

    last_failure = None

    last_locator = None

    healed_locator = None

    failure_type = None

    ai_suggestion = None