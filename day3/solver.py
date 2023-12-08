import sys

def get_input(path_to_input: str) -> list[str]:   
    with open(path_to_input) as input:
        input: list[str] = input.read().splitlines()

    return input

def adjacent_to_symbol(current_position: tuple[int, int], board: list[str]) -> bool:
    ignore_symbols: list[str] = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Check vertically
    if current_position[0] > 0 and board[current_position[0] - 1][current_position[1]] not in ignore_symbols:
        return True
    if current_position[0] < len(board) - 1 and board[current_position[0] + 1][current_position[1]] not in ignore_symbols:
        return True
    # Check horizontally
    if current_position[1] > 0 and board[current_position[0]][current_position[1] - 1] not in ignore_symbols:
        return True
    if current_position[1] < len(board[0]) - 1 and board[current_position[0]][current_position[1] + 1] not in ignore_symbols:
        return True
    # Check diagonally
    if current_position[0] > 0 and current_position[1] > 0 and board[current_position[0] - 1][current_position[1] - 1] not in ignore_symbols:
        return True
    if current_position[0] < len(board) - 1 and current_position[1] < len(board[0]) - 1 and board[current_position[0] + 1][current_position[1] + 1] not in ignore_symbols:
        return True
    if current_position[0] > 0 and current_position[1] < len(board[0]) - 1 and board[current_position[0] - 1][current_position[1] + 1] not in ignore_symbols:
        return True
    if current_position[0] < len(board) - 1 and current_position[1] > 0 and board[current_position[0] + 1][current_position[1] - 1] not in ignore_symbols:
        return True

    return False

def check_for_gears(current_position: tuple[int, int], board: list[str]) -> int:
    numbers_adjacent: int = 0
    gear_ratio: int = 1

    if current_position[0] > 0 and board[current_position[0] - 1][current_position[1]].isnumeric():
        numbers_adjacent += 1
        gear_ratio *= get_number(
            (current_position[0] - 1, current_position[1]), board)
    else:
        if current_position[0] > 0 and current_position[1] > 0 and board[current_position[0] - 1][current_position[1] - 1].isnumeric():
            numbers_adjacent += 1
            gear_ratio *= get_number(
                (current_position[0] - 1, current_position[1] - 1), board)
        if current_position[0] > 0 and current_position[1] < len(board[0]) - 1 and board[current_position[0] - 1][current_position[1] + 1].isnumeric():
            numbers_adjacent += 1
            gear_ratio *= get_number(
                (current_position[0] - 1, current_position[1] + 1), board)
    if current_position[0] < len(board) - 1 and board[current_position[0] + 1][current_position[1]].isnumeric():
        numbers_adjacent += 1
        gear_ratio *= get_number((current_position[0] + 1, current_position[1]), board)
    else:
        if current_position[0] < len(board) - 1 and current_position[1] < len(board[0]) - 1 and board[current_position[0] + 1][current_position[1] + 1].isnumeric():
            numbers_adjacent += 1
            gear_ratio *= get_number(
                (current_position[0] + 1, current_position[1] + 1), board)
        if current_position[0] < len(board) - 1 and current_position[1] > 0 and board[current_position[0] + 1][current_position[1] - 1].isnumeric():
            numbers_adjacent += 1
            gear_ratio *= get_number(
                (current_position[0] + 1, current_position[1] - 1), board)
    if current_position[1] > 0 and board[current_position[0]][current_position[1] - 1].isnumeric():
        numbers_adjacent += 1
        gear_ratio *= get_number((current_position[0], current_position[1] - 1), board)
    if current_position[1] < len(board[0]) - 1 and board[current_position[0]][current_position[1] + 1].isnumeric():
        numbers_adjacent += 1
        gear_ratio *= get_number((current_position[0], current_position[1] + 1), board)

    if numbers_adjacent == 2:
        return gear_ratio

    return 0

def get_number(current_position: tuple[int, int], board: list[str]) -> int:
    number: str = board[current_position[0]][current_position[1]]
    count: int = 1

    while current_position[1] - count >= 0 and board[current_position[0]][current_position[1] - count].isnumeric():
        number = board[current_position[0]][current_position[1] - count] + number
        count += 1
    
    count = 1

    while current_position[1] + count < len(board[0]) and board[current_position[0]][current_position[1] + count].isnumeric():
        number += board[current_position[0]][current_position[1] + count]
        count += 1

    return int(number)

def find_parts_and_gears(lines: list[str]) -> tuple[int, int]:
    part_numbers: list[int] = []
    gear_ratios: list[int] = []

    for line_number, line in enumerate(lines):
        is_part_number: bool = False
        number: str = ""

        for column_number, symbol in enumerate(line):
            if is_part_number:
                if symbol.isnumeric():
                    number += symbol
                else:
                    is_part_number = False
                    part_numbers.append(int(number))
                    number = ""
            elif symbol.isnumeric():
                is_part_number = adjacent_to_symbol((line_number, column_number), lines)
                number += symbol
            elif number != "":
                number = ""

            if symbol == "*":
                gear_ratios.append(check_for_gears((
                    line_number, column_number), lines))

        if is_part_number:
            part_numbers.append(int(number))

    return (sum(part_numbers), sum(gear_ratios))

def main() -> int:
    lines = get_input("input.txt")

    sum_part_numbers: int
    sum_gear_ratios: int
    sum_part_numbers, sum_gear_ratios = find_parts_and_gears(lines)

    print("Solution Task 1:", sum_part_numbers)
    print("Solution Task 2:", sum_gear_ratios)

    return 0

if __name__ == "__main__":
    sys.exit(main())
