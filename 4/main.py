"""Day I puzzle solutions."""

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
SMALL_INPUT_2 = pathjoin(INPUT_FOLDER, "small_input2")
INPUT = pathjoin(INPUT_FOLDER, "input")

# Puzzle constants
XMAS_CHARS = ["X", "M", "A", "S"]
# Direction constants
DIRECTIONS = {
    "TOP LEFT": (-1, -1),
    "TOP": (-1, 0),
    "TOP RIGHT": (-1, 1),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
    "BOTTOM LEFT": (1, -1),
    "BOTTOM": (1, 0),
    "BOTTOM RIGHT": (1, 1),
}


def read_input(file: str) -> list[list[str]]:
    """
    Read the input file and format the content to a list of lists of characters.

    :param str file: The input file name
    :return list[list[str]]: The formatted output
    """
    # Open the file
    with open(file, "r", encoding="utf-8") as in_file:
        lines = in_file.readlines()

    word_search = []
    # Go through each line
    for line in lines:
        # Split the line character by character and add it to the word search
        word_search.append(list(line.strip()))

    return word_search


def check_word_in_direction(
    word_search: list[list[str]],
    line_nb: int,
    col_nb: int,
    direction: tuple[int, int],
    remaining_chars: list[str],
) -> bool:
    """
    Checks if the word 'XMAS' is at the given position and direction in the grid.

    Recursive function that checks if the word 'XMAS' is in the grid at the given
    position.

    :param list[list[str]] word_search: The word search grid
    :param int line_nb: The line number of the first letter
    :param int col_nb: The column number of the first letter
    :param tuple[int, int] direction: The direction to check
    :param list[str] remaining_chars: The rmaining chars to check by the recursive
    function
    :return bool: `True` if the word is in the grid, `False` if not
    """
    try:
        cur_char = word_search[line_nb][col_nb]
    except IndexError:
        # The given indices are out of the grid
        # The word can not be in that direction
        return False

    expected_char = remaining_chars.pop(0)
    if cur_char == expected_char:
        # The current character is the expected one in the word
        if not remaining_chars:
            # We have a complete word
            return True

        # Calculate where the next character should be placed
        new_line_nb = line_nb + direction[0]
        new_col_nb = col_nb + direction[1]
        if new_line_nb < 0 or new_col_nb < 0:
            # The new indices are out of the grid
            # The word can not be in that direction
            return False

        # If we are not in these conditions keep checking the rest of the word
        return check_word_in_direction(
            word_search, new_line_nb, new_col_nb, direction, remaining_chars
        )

    else:
        # The current character is not the expected one in the word
        # Stop checking and
        return False


def check_x_mas(word_search: list[list[str]], line_nb: int, col_nb: int) -> bool:
    """
    Checks if there is an X-MAS pattern at the given position.

    :param list[list[str]] word_search: The word search grid
    :param int line_nb: The line number of the first letter
    :param int col_nb: The column number of the first letter
    :return bool: `True` if the pattern is in the grid, `False` if not
    """
    # Check if the current character is an 'A'
    cur_char = word_search[line_nb][col_nb]
    if not cur_char == "A":
        # We only check the A's because they are in the middle of the MAS cross
        return False

    # Check if the 'A' is at the border of the grid
    if not (
        0 < line_nb < len(word_search) - 1 and 0 < col_nb < len(word_search[0]) - 1
    ):
        # The 'A' is at the border of the grid
        # It is impossible to have a X-MAS pattern here
        return False

    # Check all possibilities of X-MAS patterns
    #  1        2        3        4
    # M.S      M.M      S.M      S.S
    # .A.  or  .A.  or  .A.  or  .A.
    # M.S      S.S      S.M      M.M
    is_pattern_1 = (
        word_search[line_nb - 1][col_nb - 1] == "M"
        and word_search[line_nb + 1][col_nb + 1] == "S"
        and word_search[line_nb + 1][col_nb - 1] == "M"
        and word_search[line_nb - 1][col_nb + 1] == "S"
    )
    is_pattern_2 = (
        word_search[line_nb - 1][col_nb - 1] == "M"
        and word_search[line_nb + 1][col_nb + 1] == "S"
        and word_search[line_nb + 1][col_nb - 1] == "S"
        and word_search[line_nb - 1][col_nb + 1] == "M"
    )
    is_pattern_3 = (
        word_search[line_nb - 1][col_nb - 1] == "S"
        and word_search[line_nb + 1][col_nb + 1] == "M"
        and word_search[line_nb + 1][col_nb - 1] == "S"
        and word_search[line_nb - 1][col_nb + 1] == "M"
    )
    is_pattern_4 = (
        word_search[line_nb - 1][col_nb - 1] == "S"
        and word_search[line_nb + 1][col_nb + 1] == "M"
        and word_search[line_nb + 1][col_nb - 1] == "M"
        and word_search[line_nb - 1][col_nb + 1] == "S"
    )

    return is_pattern_1 or is_pattern_2 or is_pattern_3 or is_pattern_4


def puzzle1(file: str) -> int:
    """
    Solves the first puzzle.

    :param str file: The input file
    :return int: The puzzle solution for the given input
    """
    # Load the input
    word_search = read_input(file)

    nb_xmas = 0
    # Go through each character in the word search grid
    for line_nb, line in enumerate(word_search):
        for col_nb, _ in enumerate(line):
            # For each character check each direction
            for direction_name, direction in DIRECTIONS.items():
                # Check if the word is in the grid in the current direction
                if check_word_in_direction(
                    word_search, line_nb, col_nb, direction, XMAS_CHARS.copy()
                ):
                    # The word has been found starting from that position and in that direction
                    logger.info(
                        "The word 'XMAS' was found starting from [%s, %s] in %s direction",
                        line_nb,
                        col_nb,
                        direction_name,
                    )
                    nb_xmas += 1

    # Return the solution
    return nb_xmas


def puzzle2(file: str) -> int:
    """
    Solves the second puzzle.

    :param str file: The input file
    :return int: The puzzle solution for the given input
    """
    # Load the input
    word_search = read_input(file)

    nb_x_mas = 0
    # Go through each character in the word search grid
    for line_nb, line in enumerate(word_search):
        for col_nb, _ in enumerate(line):
            # Check if the pattern is in the grid at this position
            if check_x_mas(word_search, line_nb, col_nb):
                # The pattern has been found with the 'A' being at that position
                logger.info(
                    "The 'X-MAS' pattern was found with the 'A' being at position [%s, %s]",
                    line_nb,
                    col_nb,
                )
                nb_x_mas += 1

    # Return the solution
    return nb_x_mas


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
