import sys

CACHE: dict[tuple[str], tuple[str]] = {}

def get_input(path_to_input: str) -> tuple[str]:   
    with open(path_to_input) as input:
        input: tuple[str] = tuple(input.read().splitlines())

    return input

def tilt_north(field: tuple[str]) -> tuple[str]:
    field_copy: list[str] = [[*line] for line in field]

    for column in range(len(field_copy[0])):
        number_of_rocks: list[int] = [0]
        count: int = 0

        for row in range(len(field_copy)):
            if field_copy[row][column] == "O":
                number_of_rocks[count] += 1
                field_copy[row][column] = "."
            elif field_copy[row][column] == "#":
                count += 1
                number_of_rocks.append(0)

        count = 0

        for row in range(len(field_copy)):
            if field_copy[row][column] == "#":
                count += 1
            elif number_of_rocks[count] > 0:
                field_copy[row][column] = "O"
                number_of_rocks[count] -= 1

    return tuple(["".join(line) for line in field_copy])

def tilt_south(field: tuple[str]) -> tuple[str]:
    field_copy: list[str] = [[*line] for line in field]

    for column in range(len(field_copy[0])):
        number_of_rocks: list[int] = [0]
        count: int = 0

        for row in reversed(range(len(field_copy))):
            if field_copy[row][column] == "O":
                number_of_rocks[count] += 1
                field_copy[row][column] = "."
            elif field_copy[row][column] == "#":
                count += 1
                number_of_rocks.append(0)

        count = 0

        for row in reversed(range(len(field_copy))):
            if field_copy[row][column] == "#":
                count += 1
            elif number_of_rocks[count] > 0:
                field_copy[row][column] = "O"
                number_of_rocks[count] -= 1

    return tuple(["".join(line) for line in field_copy])

def tilt_east(field: tuple[str]) -> tuple[str]:
    field_copy: list[str] = [[*line] for line in field]

    for row in range(len(field_copy)):
        number_of_rocks: list[int] = [0]
        count: int = 0

        for column in reversed(range(len(field_copy[0]))):
            if field_copy[row][column] == "O":
                number_of_rocks[count] += 1
                field_copy[row][column] = "."
            elif field_copy[row][column] == "#":
                count += 1
                number_of_rocks.append(0)

        count = 0

        for column in reversed(range(len(field_copy[0]))):
            if field_copy[row][column] == "#":
                count += 1
            elif number_of_rocks[count] > 0:
                field_copy[row][column] = "O"
                number_of_rocks[count] -= 1

    return tuple(["".join(line) for line in field_copy])

def tilt_west(field: tuple[str]) -> tuple[str]:
    field_copy: list[str] = [[*line] for line in field]

    for row in range(len(field_copy)):
        number_of_rocks: list[int] = [0]
        count: int = 0

        for column in range(len(field_copy[0])):
            if field_copy[row][column] == "O":
                number_of_rocks[count] += 1
                field_copy[row][column] = "."
            elif field_copy[row][column] == "#":
                count += 1
                number_of_rocks.append(0)

        count = 0

        for column in range(len(field_copy[0])):
            if field_copy[row][column] == "#":
                count += 1
            elif number_of_rocks[count] > 0:
                field_copy[row][column] = "O"
                number_of_rocks[count] -= 1

    return tuple(["".join(line) for line in field_copy])

def calculate_total_load(field: tuple[str]) -> int:
    total_load: int = 0

    for count, line in enumerate(field):
        total_load += line.count("O") * (len(field) - count)

    return total_load

def rotate(field: tuple[str]) -> tuple[str]:
    if field in CACHE:
        return CACHE[field]

    field_copy: tuple[str] = tilt_north(field)
    field_copy = tilt_west(field_copy)
    field_copy = tilt_south(field_copy)
    field_copy = tilt_east(field_copy)

    CACHE[field] = field_copy

    return field_copy

def rotate_n_times(field: tuple[str], number_of_rotations: int) -> tuple[str]:
    field_copy: tuple[str] = rotate(field)

    for _ in range(number_of_rotations - 1):
        field_copy = rotate(field_copy)

    return field_copy

def main() -> int:
    field: tuple[str] = get_input("input.txt")

    # Part 1
    tilted_field: tuple[str] = tilt_north(field)
    total_load_1: int = calculate_total_load(tilted_field)

    print("Solution Task 1", total_load_1)

    # Part 2
    field_part_2: tuple[str] = rotate_n_times(field, 10**9)
    total_load_2: int = calculate_total_load(field_part_2)

    print("Solution Part 2:", total_load_2)

    return 0

if __name__ == "__main__":
    sys.exit(main())
