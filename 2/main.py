"""Day 2 puzzle solutions."""

import logging
from os.path import dirname
from os.path import join as pathjoin

# Load and configure the logger
LOG_FORMAT = "%(levelname)s - %(name)s : %(message)s"
logging.basicConfig(
    level=logging.INFO, handlers=[logging.StreamHandler()], format=LOG_FORMAT
)
logger = logging.getLogger(__name__)

# Constants for the input paths
INPUT_FOLDER = pathjoin(dirname(__file__), "inputs")
SMALL_INPUT = pathjoin(INPUT_FOLDER, "small_input")
INPUT = pathjoin(INPUT_FOLDER, "input")


def read_input(file: str) -> list[list[int]]:
    """
    Read the input file and format the content to a list of reports.

    Each report contains a list of levels (integers).

    :param str file: The input file name
    :return list[list[int]]: The formatted output
    """
    # Open the file
    with open(file, "r", encoding="utf-8") as in_file:
        lines = in_file.readlines()

    # Each line is a report containing a list of levels (integers)
    reports = []
    for line in lines:
        # Read each report by splitting the line by spaces
        # and converting each level to an int
        report = [int(level.strip()) for level in line.split()]
        logger.debug("Created report : %s", report)
        reports.append(report)

    return reports


def is_safe(report: list[int]) -> bool:
    """
    Check if a report is safe.

    A report is safe if the list of levels it contains is stricly ascending or
    descending and that the difference between two adjacent levels is between
    1 and 3.

    :param list[int] report: The list of levels of the report
    :return bool: `True` if the report is safe, `False` if not.
    """
    # If the report contains only 1 level it is safe
    report_len = len(report)
    if report_len < 2:
        return True

    # Start the level counters
    level_1 = 0
    level_2 = 1

    # Set up the expected order of the list from the 2 first elements
    # (1 when ascending and -1 when descending)
    if report[level_1] <= report[level_2]:
        order = 1
    else:
        order = -1

    # Go through each level
    while level_2 < report_len:
        # Calculate the difference between the 2 adjacent levels
        level_diff = report[level_2] - report[level_1]
        # Check that the order is respected (multiplication by order)
        # and that the difference is between 1 and 3
        if not 1 <= level_diff * order <= 3:
            logger.debug(
                "Report %s is unsafe at adjacent levels %s - %s "
                "(expected order was %s)",
                report,
                report[level_1],
                report[level_2],
                "ascending" if order == 1 else "descending",
            )
            # If a rule is not respected, return False
            return False

        # Increment levels
        level_1 += 1
        level_2 += 1

    # The rules are respected for all adjacent levels in the report, return True
    return True


def puzzle1(file: str) -> int:
    """
    Solves the first puzzle.

    :param str file: The input file
    :return int: The puzzle solution for the given input
    """
    # Load the input
    reports = read_input(file)

    # Go through each report of the list
    safe_reports = 0
    for report in reports:
        if is_safe(report):
            logger.debug("Report %s is safe", report)
            safe_reports += 1

    # Return the solution
    return safe_reports


def puzzle2(file: str) -> int:
    """
    Solves the second puzzle.

    :param str file: The input file
    :return int: The puzzle solution for the given input
    """
    # Load the input
    _ = read_input(file)

    # Return the solution
    return 0


def main() -> None:
    """
    Main function
    """
    ### First part of the problem
    res1 = puzzle1(INPUT)
    print(f"First part result : {res1}")

    ### Second part of the problem
    res2 = puzzle2(SMALL_INPUT)
    print(f"Second part result : {res2}")


if __name__ == "__main__":
    main()
