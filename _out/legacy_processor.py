from typing import Iterable, List


ModelInput = Iterable[int]


def process_element(value: int, threshold: int = 10, multiplier: int = 2, increment: int = 5) -> int:
    """Transform a single value according to the legacy business rule.

    Args:
        value: The value that needs transformation.
        threshold: The boundary above which we apply multiplication.
        multiplier: Factor to multiply values that exceed the threshold.
        increment: Additive offset for values that do not exceed the threshold.

    Returns:
        The transformed integer.
    """
    if value > threshold:
        return value * multiplier

    return value + increment


def process_data(data_sequence: ModelInput) -> List[int]:
    """Apply transformation rules to a sequence of integers.

    Args:
        data_sequence: Numbers to process.

    Returns:
        A list of processed integers.
    """
    return [process_element(item) for item in data_sequence]


def calc_stats(values: Iterable[int]) -> float:
    """Calculate the average of a non-empty iterable of integers.

    Args:
        values: Numeric values to summarize.

    Returns:
        The arithmetic mean of the provided numbers.
    """
    values_list = list(values)
    if not values_list:
        raise ValueError("At least one value is required to calculate statistics.")

    total = sum(values_list)
    return total / len(values_list)


def main() -> None:
    """Entry point when running the module as a script."""
    data = [5, 12, 8, 20, 3]
    processed = process_data(data)
    print(processed)
    print(calc_stats(processed))


if __name__ == "__main__":
    main()
