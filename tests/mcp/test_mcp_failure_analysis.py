# tests/mcp/test_mcp_failure_analysis.py

import pytest

from mcp.failure_analyzer import (
    LLMFailureAnalyzer
)


@pytest.mark.mcp
def test_mcp_failure_analysis():

    error = (                      
        "TimeoutException: "          #fake erroer message to simulate a failure scenario for testing the failure analysis functionality
        "Element not found"
    )

    result = (                     #calling the failure analyzer to analyze the simulated error and generate an AI response based on it
        LLMFailureAnalyzer
        .analyze(error)
    )

    assert (
        "AI Response Generated"
        in result
    )