"""Day 1 puzzle solutions."""

import logging

import numpy as np

# Load and configure the logger
LOG_FORMAT = "%(levelname)s - %(name)s : %(message)s"
logging.basicConfig(
    level=logging.INFO, handlers=[logging.StreamHandler()], format=LOG_FORMAT
)
logger = logging.getLogger(__name__)


def read_input(file: str) -> tuple[np.ndarray, np.ndarray]:
    """
    Read the input file and format the content to a tuple of lists.

    :param str file: The input file name
    :return tuple[np.ndarray, np.ndarray]: The formatted output
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

    # Create numpy arrays for both lists (easier to manipulate)
    np_left = np.array(left)
    np_right = np.array(right)

    # Log the formatted input
    logger.debug("Left list : %s", np_left)
    logger.debug("Right list : %s", np_right)

    return (np_left, np_right)


def puzzle1(file: str) -> int:
    """
    Solves the first puzzle.

    :param str file: The input file
    :return int: The puzzle solution for the given input
    """
    # Load the input
    left, right = read_input(file)

    # Sort the numpy arrays
    sorted_left = np.sort(left)
    sorted_right = np.sort(right)
    logger.debug("Numpy array sorted for left list: %s", sorted_left)
    logger.debug("Numpy array sorted for right list: %s", sorted_right)

    # Get an absolute difference array from the 2 lists
    np_abs_diff = np.abs(sorted_left - sorted_right)
    logger.debug("Absolute difference array: %s", np_abs_diff)
    # Get the sum of all the differences
    np_sum = np.sum(np_abs_diff)
    logger.debug("Sum of the absolute differences: %s", np_sum)

    return np_sum


def puzzle2(file: str) -> int:
    """
    Solves the second puzzle.

    :param str file: The input file
    :return int: The puzzle solution for the given input
    """
    # Load the input
    left, right = read_input(file)

    # Start the similarity score at 0
    similarity_score = 0

    # Go through each element of the left list
    for left_pos in left:
        # Extract all the positions from the right list that are equal
        # to the current left position and count them
        # shape[0] is the same as the len of a 1D-array
        right_pos_count = np.extract(right == left_pos, right).shape[0]
        logger.debug(
            "Appearances of the left position '%s' in the right list : %s",
            left_pos,
            right_pos_count,
        )

        # Calculate the similarity score
        similarity_score += left_pos * right_pos_count
        logger.debug("Current similarity score is : %s", similarity_score)

    logger.debug("Final similarity score : %s", similarity_score)

    return similarity_score


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
