from datetime import datetime


def calculator_tool(expression):
    try:
        result = eval(expression)
        return f"Calculated Result: {result}"
    except:
        return "Invalid mathematical expression."


def weather_tool(city="Mumbai"):
    # Mock weather tool
    weather_data = {
        "mumbai": "28°C, Humid",
        "delhi": "24°C, Clear",
        "bangalore": "22°C, Pleasant"
    }

    return f"Weather in {city.title()}: {weather_data.get(city.lower(), 'Data not available')}"


def summarizer_tool(text):
    words = text.split()
    summary = " ".join(words[:10])
    return f"Summary: {summary}..."