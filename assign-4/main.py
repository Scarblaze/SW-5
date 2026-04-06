from planner import Planner
from executor import Executor


def main():
    planner = Planner()
    executor = Executor()

    print("=== Multi-Step Planning Agent ===")

    while True:
        user_input = input("Enter query: ").strip()

        if user_input.lower() == "exit":
            break

        plan = planner.create_plan(user_input)
        numbers = planner.extract_numbers(user_input)

        outputs, final_result = executor.execute(plan, numbers)

        print("\nExecution Plan:")
        for step in plan:
            print(f"- {step}")

        print("\nIntermediate Outputs:")
        for key, value in outputs.items():
            print(f"{key}: {value}")

        print("\nFinal Output:")
        print(final_result)


if __name__ == "__main__":
    main()