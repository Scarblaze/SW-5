from llm_agent import LLMAgent


def main():
    agent = LLMAgent()

    print("=== LLM Based Agent ===")

    while True:
        user_input = input("Enter command: ").strip()

        if user_input.lower() == "exit":
            break

        result = agent.execute(user_input)
        print(result)


if __name__ == "__main__":
    main()