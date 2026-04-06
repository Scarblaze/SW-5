from langchain_core.prompts import PromptTemplate
import re


class Planner:
    def __init__(self):
        self.prompt = PromptTemplate.from_template(
            """
            Break the following task into executable steps:
            {query}
            """
        )

    def create_plan(self, query):
        query_lower = query.lower()
        steps = ["extract_numbers"]

        if "average" in query_lower:
            steps.append("compute_average")

        elif "sum" in query_lower:
            steps.append("compute_sum")

        elif "maximum" in query_lower or "max" in query_lower:
            steps.append("compute_max")

        elif "minimum" in query_lower or "min" in query_lower:
            steps.append("compute_min")

        if "summarize" in query_lower:
            steps.append("generate_summary")

        return steps

    def extract_numbers(self, text):
        return list(map(int, re.findall(r"\d+", text)))