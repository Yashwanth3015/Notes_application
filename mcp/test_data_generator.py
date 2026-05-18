#instead of hardcoding test data, we generate dynamic data for testing using this utility class.
# This ensures unique data for each test run and prevents conflicts with existing data in the system.
import time


class MCPTestDataGenerator:

    @staticmethod
    def generate_note():

        timestamp = int(time.time())

        return {
            "title": f"MCP_Note_{timestamp}",
            "description": (
                f"Generated MCP note "
                f"{timestamp}"
            ),
            "category": "Work"
        }