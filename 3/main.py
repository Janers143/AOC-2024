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
SMALL_INPUT_2 = pathjoin(INPUT_FOLDER, "small_input2")
INPUT = pathjoin(INPUT_FOLDER, "input")

# Puzzle constants
MUL_START = "mul("
MUL_END = ")"
DO_STR = "do()"
DONT_STR = "don't()"


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


def get_regex_matches(lines: list[str], regex: str) -> list[str]:
    """Get the list of all the substrings that match the regex in the given lines.

    :param list[str] lines: The list of lines of the input
    :param str regex: The regex to match
    :return list[str]: The list of substrings that match the regex
    """
    substrings_match = []

    # Go through each line of the input
    for line in lines:
        # Get all the substrings that match the regex
        regex_matchs = re.compile(regex).findall(line)
        # Add the list of substrings in the line to the complete list
        substrings_match.extend(regex_matchs)

    return substrings_match


def calculate_mul_result(mul_string: str) -> int:
    """
    Parse the mul string and calculate the result of the multiplication

    :param str mul_string: The mul string
    :return int: The result of the multiplication
    """
    logger.debug("Calculating %s", mul_string)
    val_1, val_2 = [
        int(value) for value in mul_string.lstrip(MUL_START).rstrip(MUL_END).split(",")
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

    # The regex that matches mul strings
    regex = r"mul\(\d{1,3},\d{1,3}\)"

    # Get the multiplication strings from the input lines
    mul_strings = get_regex_matches(input_lines, regex)
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
    input_lines = read_input(file)

    # The regex that matches mul, dos and don'ts strings
    regex = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

    # Get the multiplication strings from the input lines
    mul_dos_donts = get_regex_matches(input_lines, regex)
    logger.debug("Found %s instructions in the given input", len(mul_dos_donts))

    sum_of_mul = 0
    enabled = True
    # Go through each instruction of the list
    for instruction in mul_dos_donts:
        if instruction == DO_STR:
            # The instruction is do(), enable the mul calculation
            enabled = True
            logger.debug("The mul calculation is ENABLED")
        elif instruction == DONT_STR:
            # The instruction is don't(), disable the mul calculation
            enabled = False
            logger.debug("The mul calculation is DISABLED")
        elif enabled:
            # The instruction is a mul() and the calculation is enabled
            # Calculate the multiplication result
            mul_result = calculate_mul_result(instruction)
            # Add the result of the multiplication to the total sum
            sum_of_mul += mul_result
        else:
            # The instruction is a mul() but the calculation is disabled
            logger.debug("The mul() instruction '%s' is skipped", instruction)

    # Return the solution
    return sum_of_mul


def main() -> None:
    """
    Main function
    """
    ### First part of the problem
    res1 = puzzle1(INPUT)
    print(f"First part result : {res1}")

    ### Second part of the problem
    res2 = puzzle2(INPUT)
    print(f"Second part result : {res2}")


if __name__ == "__main__":
    main()
