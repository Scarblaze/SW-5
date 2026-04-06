from google import genai
from tools import calculator_tool, weather_tool, summarizer_tool


client = genai.Client(api_key="AIzaSyB6_2YNCEmAiDYXjgcKPfGqZ3sEdU2x3Z0")


class LLMAgent:
    def decide_tool(self, user_input):
        prompt = f"""
        Choose best tool:
        calculator
        weather
        summarizer

        Query: {user_input}
        """

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            return response.text.strip().lower()

        except Exception:
            # fallback simulated LLM reasoning
            text = user_input.lower()

            if any(op in text for op in ["+", "-", "*", "/", "calculate"]):
                return "calculator"
            elif "weather" in text:
                return "weather"
            elif "summarize" in text:
                return "summarizer"

            return "unknown"

    def execute(self, user_input):
        tool = self.decide_tool(user_input)

        if "calculator" in tool:
            expression = user_input.replace("calculate", "").strip()
            result = calculator_tool(expression)

        elif "weather" in tool:
            city = user_input.split()[-1]
            result = weather_tool(city)

        elif "summarizer" in tool:
            text = user_input.replace("summarize", "").strip()
            result = summarizer_tool(text)

        else:
            result = "No suitable tool selected."

        self.log_interaction(user_input, tool, result)
        return result

    def log_interaction(self, user_input, tool, output):
        with open("logs.txt", "a") as f:
            f.write(f"INPUT: {user_input}\n")
            f.write(f"TOOL: {tool}\n")
            f.write(f"OUTPUT: {output}\n")
            f.write("-" * 50 + "\n")