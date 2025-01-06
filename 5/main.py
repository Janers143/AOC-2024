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
INPUT = pathjoin(INPUT_FOLDER, "input")


def read_input(file: str) -> tuple[dict[int, list[int]], list[list[int]]]:
    """
    Read the input file and format the content to ordering rules and updates.

    The output format is a tuple containing:
    - a dict representing the ordering rules: each key is a page and the value
    is the list of pages it can not precede
    - a list of updates: each update is the list of pages in the order of impression

    :param str file: The input file name
    :return tuple[dict[int, list[int]], list[list[int]]]: The formatted output
    """
    # Open the file
    with open(file, "r", encoding="utf-8") as in_file:
        lines = map(lambda file_line: file_line.strip(), in_file.readlines())

    ordering_rules: dict[int, list[int]] = {}
    updates = []
    # Start by reading ordering rule block
    ordering_rule_block = True
    # Go through each line
    for line in lines:
        if not line:
            # Finished reading the ordering block, start reading the updates
            ordering_rule_block = False
            continue

        if ordering_rule_block:
            # Reading an ordering rule line
            # Get the page numbers of the rule
            first_page, second_page = [int(page) for page in line.split("|")]
            if second_page in ordering_rules:
                # The succeeding page already has rules
                ordering_rules[second_page].append(first_page)
            else:
                # The succeeding page had no rules yet
                ordering_rules[second_page] = [first_page]
        else:
            # Reading an update line
            # Add the update to the update list
            update = [int(page) for page in line.split(",")]
            updates.append(update)

    return ordering_rules, updates


def check_update_validity(
    ordering_rules: dict[int, list[int]], update: list[int]
) -> bool:
    """
    Check if an update is valid according to ordering rules.

    :param dict[int, list[int]] ordering_rules: The ordering rule
    :param list[int] update: The update to check
    :return bool: `True` if the update is valid, `False` if not
    """
    logger.debug("Checking update: %s", update)
    # Go through each page in the update list
    for page_id, page in enumerate(update):
        # Get the list of pages the current page can not preceed
        cant_preceed_list = ordering_rules.get(page, [])
        for cant_preceed_page in cant_preceed_list:
            # Check that there's no page that must preceed
            # the current page in the rest of the list
            if cant_preceed_page in update[page_id + 1 :]:
                # An ordering rule was not respected
                logger.debug(
                    "An ordering rule was not respected: %s comes before %s",
                    page,
                    cant_preceed_page,
                )
                return False

    # The whole list was checked and no rule was broken
    logger.debug("The update %s is valid", update)
    return True


def get_updates_score(updates: list[int]) -> int:
    """
    Get the score from a list of updates.

    The score is obtained by adding up the middle value of each update.

    :param list[int] updates: The list of updates to consider
    :return int: The score
    """
    updates_score = 0
    # Go through each update
    for update in updates:
        # Get the middle value of the update and add it to the update score
        updates_score += update[len(update) // 2]

    return updates_score


def puzzle1(file: str) -> int:
    """
    Solves the first puzzle.

    :param str file: The input file
    :return int: The puzzle solution for the given input
    """
    # Load the input
    ordering_rules, updates = read_input(file)

    valid_updates = []
    # Go through each update
    for update in updates:
        if check_update_validity(ordering_rules, update):
            # The update is valid, add it to the valid updates list
            valid_updates.append(update)

    # Return the solution
    return get_updates_score(valid_updates)


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
