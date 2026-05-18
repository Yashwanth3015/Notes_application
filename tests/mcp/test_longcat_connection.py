from mcp.llm_client import LLMClient


def test_longcat_connection():

    prompt = """

Suggest XPath locator
for login button.
"""

    result = LLMClient.generate(
        prompt
    )

    print("\n")
    print("=" * 60)
    print("LONGCAT FINAL OUTPUT")
    print("=" * 60)

    print(result)

    print("=" * 60)

    assert result is not None