import sys

CACHE: dict[tuple[tuple[int], str], int] = {}

def get_input(path_to_input: str) -> list[str]:   
    with open(path_to_input) as input:
        input: list[str] = input.read().splitlines()

    return input

def get_number_of_damaged_springs(input: list[str]) -> list[list[int]]:
    return [[int(number) for number in line.split()[1].split(",")] for line in input]

def get_rows(input: list[str]) -> list[str]:
    return[line.split()[0] for line in input]

def unfold_springs_and_rows(number_of_springs: list[list[int]],
                            rows: list[str]) -> tuple[list[list[int]], list[str]]:
    return ([springs * 5 for springs in number_of_springs],
            ["?".join([row] * 5) for row in rows])

def number_of_arrangements_one_line(number_of_springs: list[int], row: str) -> int:
    if row == "":
        return 1 if number_of_springs == [] else 0
    if number_of_springs == []:
        return 0 if "#" in row else 1

    cache_key: tuple[tuple[int], str] = (tuple(number_of_springs), row)

    if cache_key in CACHE:
        return CACHE[cache_key]

    arrangements: int = 0

    if row[0] in ".?":
        arrangements += number_of_arrangements_one_line(number_of_springs, row[1:])

    if row[0] in "#?":
        if number_of_springs[0] <= len(row) and "." not in row[:number_of_springs[0]]:
            if number_of_springs[0] == len(row) or row[number_of_springs[0]] != "#":
                arrangements += number_of_arrangements_one_line(
                    number_of_springs[1:], row[number_of_springs[0] + 1:] 
                )

    CACHE[cache_key] = arrangements

    return arrangements

def all_possible_arrangements(number_of_springs: list[list[int]],
                              rows: list[str]) -> int:
    sum_all_arrangements: int = 0

    for springs, row in zip(number_of_springs, rows):
        sum_all_arrangements += number_of_arrangements_one_line(springs, row)

    return sum_all_arrangements

def main() -> int:
    input: list[str] = get_input("input.txt")
    damaged_springs: list[list[int]] = get_number_of_damaged_springs(input)
    rows: list[str] = get_rows(input)

    # Part 1
    sum_all_arrangements = all_possible_arrangements(damaged_springs, rows)

    print("Solution Task 1:", sum_all_arrangements)

    # Part 2
    springs_unfolded: list[list[int]]
    rows_unfolded: list[str]
    springs_unfolded, rows_unfolded = unfold_springs_and_rows(damaged_springs, rows)

    sum_all_arrangements_unfolded: int = all_possible_arrangements(
        springs_unfolded, rows_unfolded)

    print("Solution Task 2:", sum_all_arrangements_unfolded)

    return 0

if __name__ == "__main__":
    sys.exit(main())
