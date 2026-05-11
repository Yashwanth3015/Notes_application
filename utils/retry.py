import time


def retry_action(action, retries=3):        #it performs automatic retry of a given action

    for attempt in range(retries):

        try:
            return action()

        except Exception:

            time.sleep(2)

    raise Exception("Action failed after retries")                      