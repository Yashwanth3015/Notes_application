# mcp/failure_analyzer.py

from mcp.llm_client import LLMClient #import stimuted LLM client for generating AI responses based on failure analysis


class LLMFailureAnalyzer:

    @staticmethod
    def analyze(exception):

        prompt = f"""
        Analyze Selenium/API failure:

        {str(exception)}

        Suggest possible fix.
        """

        return LLMClient.generate(prompt)