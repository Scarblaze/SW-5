from datetime import datetime


def execute_action(intent, user_input):
    if intent == "calculate":
        try:
            expression = user_input.replace("calculate", "").strip()
            result = eval(expression)
            return f"Result: {result}"
        except:
            return "Invalid calculation expression."

    elif intent == "date":
        return f"Today's date is: {datetime.now().date()}"

    elif intent == "greeting":
        return "Hello! How can I assist you?"

    else:
        return "Sorry, I do not understand the command."