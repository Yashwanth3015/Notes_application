import pytest

from mcp.failure_analyzer import (
    LLMFailureAnalyzer
)


@pytest.mark.mcp
def test_mcp_failure_analysis():

    # -----------------------------------------
    # FAILURE
    # -----------------------------------------

    error = (
        "TimeoutException: "
        "Element not found"
    )

    # -----------------------------------------
    # LOCATOR
    # -----------------------------------------

    locator = (
        "//button[@type='submit']"
    )

    # -----------------------------------------
    # MCP FAILURE ANALYSIS
    # -----------------------------------------

    result = (
        LLMFailureAnalyzer
        .analyze(
            error,
            locator
        )
    )

    print("\nAI Analysis:")
    print(result)

    # -----------------------------------------
    # VALIDATION
    # -----------------------------------------

    assert result is not None