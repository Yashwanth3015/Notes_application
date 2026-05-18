from mcp.llm_client import LLMClient


class LLMFailureAnalyzer:

    @staticmethod
    def analyze(exception, locator):

        prompt = f"""

You are Selenium AI locator healer.

Original Locator:
{locator}

Failure:
{str(exception)}

STRICT RULES:
1. Return ONLY ONE VALID XPath locator.
2. Do NOT explain.
3. Do NOT return paragraphs.
4. Do NOT return markdown.
5. Output ONLY raw XPath.

Example:
 //button[contains(text(),'Login')]

"""

        return (
            LLMClient
            .generate(prompt)
            .strip()
        )