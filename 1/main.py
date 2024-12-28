"""Day 1 puzzle solutions."""

import logging

import numpy as np

# Load the logger
LOG_FORMAT = "%(levelname)s - %(name)s : %(message)s"
logging.basicConfig(
    level=logging.INFO, handlers=[logging.StreamHandler()], format=LOG_FORMAT
)
logger = logging.getLogger(__name__)


def read_input(file: str) -> tuple[list, list]:
    """
    Read the input file and format the content to a tuple of lists.

    :param str file: The input file name
    :return tuple[list, list]: The formatted output
    """
    # Open the file
    with open(file, "r", encoding="utf-8") as in_file:
        lines = in_file.readlines()

    left, right = [], []
    # Read line by line
    for line in lines:
        # Split the line in 2 and cast both positions to int
        left_pos, right_pos = [int(position.strip()) for position in line.split()]
        # Add left position to left list and right position to right list
        left.append(left_pos)
        right.append(right_pos)

    # Log the formatted input
    logging.debug("Left list : %s", left)
    logging.debug("Right list : %s", right)

    return (left, right)


def puzzle1(file: str) -> int:
    """
    Solves the first puzzle.

    :param str file: The input file
    :return int: The puzzle solution for the given input
    """
    left, right = read_input(file)

    # Sort the list and create a numpy array
    np_left = np.array(sorted(left))
    np_right = np.array(sorted(right))
    logger.debug("Numpy array sorted for left list: %s", np_left)
    logger.debug("Numpy array sorted for right list: %s", np_right)

    # Get an absolute difference array from the 2 lists
    np_abs_diff = np.abs(np_left - np_right)
    logger.debug("Absolute difference array: %s", np_abs_diff)
    # Get the sum of all the differences
    np_sum = np.sum(np_abs_diff)
    logger.debug("Sum of the absolute differences: %s", np_sum)

    return np_sum


def puzzle2(file: str) -> int:
    pass


def main() -> None:
    """
    Main function
    """
    ### First part of the problem
    res1 = puzzle1("input")
    print(f"First part result : {res1}")

    ### Second part of the problem
    res2 = puzzle2("input")
    print(f"Second part result : {res2}")


if __name__ == "__main__":
    main()
