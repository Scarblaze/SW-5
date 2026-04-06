class Executor:
    def execute(self, plan, numbers):
        intermediate_outputs = {}
        result = None

        for step in plan:
            if step == "extract_numbers":
                intermediate_outputs["numbers"] = numbers

            elif step == "compute_average":
                avg = sum(numbers) / len(numbers)
                intermediate_outputs["average"] = avg
                result = avg

            elif step == "generate_summary":
                summary = f"The average of the given numbers is {result}."
                intermediate_outputs["summary"] = summary
                result = summary

        return intermediate_outputs, result