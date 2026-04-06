from tools import calculator_tool, weather_tool, summarizer_tool


class ToolUsingAgent:
    def decide_and_execute(self, user_input):
        user_input = user_input.lower()

        if user_input.startswith("calculate"):
            expression = user_input.replace("calculate", "").strip()
            return calculator_tool(expression)

        elif user_input.startswith("weather"):
            parts = user_input.split()
            city = parts[1] if len(parts) > 1 else "Mumbai"
            return weather_tool(city)

        elif user_input.startswith("summarize"):
            text = user_input.replace("summarize", "").strip()
            return summarizer_tool(text)

        else:
            return "No suitable tool found."