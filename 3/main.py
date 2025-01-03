"""Day 3 puzzle solutions."""

import logging
import re
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


def read_input(file: str) -> list[str]:
    """
    Read the input file and format the content to a list of strings.

    :param str file: The input file name
    :return Any: The formatted output
    """
    # Open the file
    with open(file, "r", encoding="utf-8") as in_file:
        lines = in_file.readlines()

    return lines


def get_mul_strings(lines: list[str]) -> list[str]:
    """
    Find mul strings in the input (a list of strings) by using a regex.

    A mul string is a string formated as `mul(a,b)` with a and b being two
    numbers going from 1 to 999.

    :param list[str] lines: The list of lines of the input
    :return list[str]: The list of found mul strings
    """
    regex = r"mul\(\d{1,3},\d{1,3}\)"

    mul_strings = []
    # Go through each line of the input
    for line in lines:
        # Get all the substrings that match the regex
        regex_matchs = re.compile(regex).findall(line)
        # Add the list of mul strings in the line to the complete list
        mul_strings.extend(regex_matchs)

    return mul_strings


def calculate_mul_result(mul_string: str) -> int:
    """
    Parse the mul string and calculate the result of the multiplication

    :param str mul_string: The mul string
    :return int: The result of the multiplication
    """
    logger.debug("Calculating %s", mul_string)
    val_1, val_2 = [
        int(value) for value in mul_string.lstrip("mul(").rstrip(")").split(",")
    ]
    result = val_1 * val_2
    logger.debug("The result of %s * %s is %s", val_1, val_2, result)
    return result


def puzzle1(file: str) -> int:
    """
    Solves the first puzzle.

    :param str file: The input file
    :return int: The puzzle solution for the given input
    """
    # Load the input
    input_lines = read_input(file)

    # Get the multiplication strings from the input lines
    mul_strings = get_mul_strings(input_lines)
    logger.debug("Found %s mul strings in the given input", len(mul_strings))

    sum_of_mul = 0
    # Go through each mul string of the list
    for mul_str in mul_strings:
        # Calculate the multiplication result
        mul_result = calculate_mul_result(mul_str)
        # Add the result of the multiplication to the total sum
        sum_of_mul += mul_result

    # Return the solution
    return sum_of_mul


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
