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


def puzzle1(file: str) -> int:
    """
    Solves the first puzzle.

    :param str file: The input file
    :return int: The puzzle solution for the given input
    """
    # Load the input
    _ = read_input(file)

    # Return the solution
    return 0


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
