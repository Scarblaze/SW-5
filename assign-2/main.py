from agent import ToolUsingAgent


def main():
    agent = ToolUsingAgent()

    print("=== Tool Using AI Agent ===")

    while True:
        user_input = input("Enter command: ").strip()

        if user_input.lower() == "exit":
            print("Exiting agent...")
            break

        result = agent.decide_and_execute(user_input)
        print(result)


if __name__ == "__main__":
    main()