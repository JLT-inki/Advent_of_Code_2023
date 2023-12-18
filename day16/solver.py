import sys

def get_input(path_to_input: str) -> list[str]:   
    with open(path_to_input) as input:
        input: list[str] = input.read().splitlines()

    return input

def in_field(position: tuple[int, int], field: list[str]) -> bool:
    return (position[0] in range(0, len(field))
            and position[1] in range(0, len(field[0])))

def move(current_position: tuple[int, int], direction: str) -> tuple[int, int]:
    direction_to_movement: dict[str, tuple[int, int]] = {
        "up": (-1, 0), "left": (0, -1), "down": (1, 0), "right": (0, 1)}

    return (current_position[0] + direction_to_movement[direction][0],
            current_position[1] + direction_to_movement[direction][1])

def move_beam(current_position: tuple[int, int], field: list[str],
              energized_field: list[list[str]], direction: str,
              visited_splits: list[tuple[int, int]]):
    while in_field(current_position, field):
        energized_field[current_position[0]][current_position[1]] = "#"

        if field[current_position[0]][current_position[1]] == "/":
            if direction in ["left", "down"]:
                direction = "left" if direction == "down" else "down"
            else:
                direction = "right" if direction == "up" else "up"
        elif field[current_position[0]][current_position[1]] == "\\":
            if direction in ["left", "up"]:
                direction = "left" if direction == "up" else "up"
            else:
                direction = "right" if direction == "down" else "down"
        elif field[current_position[0]][current_position[1]] == "-":
            if direction in ["up", "down"]:
                if current_position in visited_splits:
                    break

                visited_splits.append(current_position)

                move_beam((current_position[0], current_position[1] - 1), field,
                          energized_field, "left", visited_splits)
                move_beam((current_position[0], current_position[1] + 1), field,
                          energized_field, "right", visited_splits)

                break
        elif field[current_position[0]][current_position[1]] == "|":
            if direction in ["left", "right"]:
                if current_position in visited_splits:
                    break

                visited_splits.append(current_position)

                move_beam((current_position[0] - 1, current_position[1]), field,
                          energized_field, "up", visited_splits)
                move_beam((current_position[0] + 1, current_position[1]), field,
                          energized_field, "down", visited_splits)

                break

        current_position = move(current_position, direction)

def count_enegized_tiles(energized_field: list[list[str]]) -> int:
    energized_tiles: int = 0

    for line in energized_field:
        energized_tiles += line.count("#")

    return energized_tiles

def find_most_energized_tiles(field: list[str]) -> int:
    energized_field: list[list[str]] = [
        ["." for _ in range(len(field[0]))] for __ in range(len(field))]
    energized_tiles: int = 0

    # Check top row
    for column in range(len(field[0])):
        move_beam((0, column), field, energized_field, "down", [])

        energized_tiles_tmp: int = count_enegized_tiles(energized_field)
        energized_tiles = (
            energized_tiles_tmp if energized_tiles_tmp > energized_tiles
            else energized_tiles)

        energized_field = [
            ["." for _ in range(len(field[0]))] for __ in range(len(field))]

    # Check bottom row
    for column in range(len(field[0])):
        move_beam((len(field) - 1, column), field, energized_field, "up", [])

        energized_tiles_tmp: int = count_enegized_tiles(energized_field)
        energized_tiles = (
            energized_tiles_tmp if energized_tiles_tmp > energized_tiles
            else energized_tiles)

        energized_field = [
            ["." for _ in range(len(field[0]))] for __ in range(len(field))]

    # Check left column
    for row in range(len(field)):
        move_beam((row, 0), field, energized_field, "right", [])

        energized_tiles_tmp: int = count_enegized_tiles(energized_field)
        energized_tiles = (
            energized_tiles_tmp if energized_tiles_tmp > energized_tiles
            else energized_tiles)

        energized_field = [
            ["." for _ in range(len(field[0]))] for __ in range(len(field))]

    # Check right column
    for row in range(len(field)):
        move_beam((row, len(field[0]) - 1), field, energized_field, "left", [])

        energized_tiles_tmp: int = count_enegized_tiles(energized_field)
        energized_tiles = (
            energized_tiles_tmp if energized_tiles_tmp > energized_tiles
            else energized_tiles)

        energized_field = [
            ["." for _ in range(len(field[0]))] for __ in range(len(field))]

    return energized_tiles

def main() -> int:
    contraption: list[str] = get_input("input.txt")

    # Part 1
    energized_field: list[list[str]] = [
        ["." for _ in range(len(contraption[0]))] for __ in range(len(contraption))]
    move_beam((0, 0), contraption, energized_field, "right", [])

    energized_tiles: int = count_enegized_tiles(energized_field)

    print("Solution Task 1:", energized_tiles)

    # Part 2
    largest_number_of_enegized_tiles: int = find_most_energized_tiles(contraption)

    print("Solution Task 2:", largest_number_of_enegized_tiles)

    return 0

if __name__ == "__main__":
    sys.exit(main())
