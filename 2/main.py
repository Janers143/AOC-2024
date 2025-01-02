"""Day 2 puzzle solutions."""

import logging
from os.path import dirname
from os.path import join as pathjoin

# Load and configure the logger
LOG_FORMAT = "%(levelname)s - %(name)s : %(message)s"
logging.basicConfig(
    level=logging.DEBUG, handlers=[logging.StreamHandler()], format=LOG_FORMAT
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
    res1 = puzzle1(SMALL_INPUT)
    print(f"First part result : {res1}")

    ### Second part of the problem
    res2 = puzzle2(SMALL_INPUT)
    print(f"Second part result : {res2}")


if __name__ == "__main__":
    main()
