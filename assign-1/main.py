from input_handler import get_user_input
from decision_logic import identify_intent
from action_executor import execute_action


def run_agent():
    print("=== Rule-Based AI Agent ===")

    while True:
        user_input = get_user_input()

        if user_input == "exit":
            print("Agent shutting down...")
            break

        intent = identify_intent(user_input)
        response = execute_action(intent, user_input)

        print(response)


if __name__ == "__main__":
    run_agent()