"""Day I puzzle solutions."""

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


def reorder_update(
    ordering_rules: dict[int, list[int]], update: list[int]
) -> list[int]:
    """
    Re-orders the update accordingly to ordering rules.

    :param dict[int, list[int]] ordering_rules: The ordering rule
    :param list[int] update: The update to re-order
    :return list[int]: The ordered update
    """
    ordered_update = [update[0]]
    # Go through each page of the update
    for page in update[1:]:
        placed = False
        # Get the list of pages the current page can not preceed
        cant_preceed_list = ordering_rules.get(page, [])
        # Go through each element of the ordered list
        for page_id, ordered_page in enumerate(ordered_update):
            # Check if the page can be placed at the current position
            if not ordered_page in cant_preceed_list:
                # The current page can be placed at this position
                ordered_update.insert(page_id, page)
                placed = True
                break

        # Check if the page has been placed in the ordered list
        if not placed:
            # The page has not been placed yet, put it at the end of the update
            ordered_update.append(page)

    return ordered_update


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
    ordering_rules, updates = read_input(file)

    invalid_updates = []
    # Go through each update
    for update in updates:
        if not check_update_validity(ordering_rules, update):
            # The update is valid, add it to the valid updates list
            invalid_updates.append(update)

    reordered_updates = []
    # Go through each invalid update
    for update in invalid_updates:
        # Re-order the invalid update
        reordered_update = reorder_update(ordering_rules, update)
        logger.debug("%s has been re-ordered to %s", update, reordered_update)
        reordered_updates.append(reordered_update)

    # Return the solution
    return get_updates_score(reordered_updates)


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
