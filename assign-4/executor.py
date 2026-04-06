class Executor:
    def execute(self, plan, numbers):
        outputs = {}
        result = None

        for step in plan:
            if step == "extract_numbers":
                outputs["numbers"] = numbers

            elif step == "compute_average":
                result = sum(numbers) / len(numbers)
                outputs["average"] = result

            elif step == "compute_sum":
                result = sum(numbers)
                outputs["sum"] = result

            elif step == "compute_max":
                result = max(numbers)
                outputs["maximum"] = result

            elif step == "compute_min":
                result = min(numbers)
                outputs["minimum"] = result

            elif step == "generate_summary":
                summary = f"The computed result is {result}."
                outputs["summary"] = summary
                result = summary

        return outputs, result