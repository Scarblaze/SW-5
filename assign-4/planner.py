from langchain_core.prompts import PromptTemplate


class Planner:
    def __init__(self):
        self.prompt = PromptTemplate.from_template(
            """
            Break the following task into steps:
            {query}
            """
        )

    def create_plan(self, query):
        query_lower = query.lower()
        steps = []

        if "average" in query_lower:
            steps.append("extract_numbers")
            steps.append("compute_average")

        if "summarize" in query_lower:
            steps.append("generate_summary")

        return steps

    def extract_numbers(self, text):
        import re
        return list(map(int, re.findall(r"\d+", text)))