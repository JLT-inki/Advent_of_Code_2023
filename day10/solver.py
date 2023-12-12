import sys

def get_input(path_to_input: str) -> list[str]:   
    with open(path_to_input) as input:
        input: list[str] = input.read().splitlines()

    return input

def get_starting_position(field: list[str]) -> tuple[int, int]:
    for number, line in enumerate(field):
        if "S" in line:
            starting_position: tuple[int, int] = (number, line.index("S"))
            break

    return starting_position

def get_starting_field(field: list[str], starting_position: tuple[int, int]) -> str:
    directions: list[str] = ["0" for _ in range(4)]
    directions_to_field: dict[str, str] = {"1100" : "|", "1010": "J", "1001": "L", "0110": "7",
                                           "0101": "F", "0011": "-"}

    if starting_position[0] - 1 >= 0 and field[starting_position[0] - 1][starting_position[1]] in ["|", "F", "7"]:
        directions[0] = "1"
    if starting_position[0] + 1 < len(field) and field[starting_position[0] + 1][starting_position[1]] in ["|", "L", "J"]:
        directions[1] = "1"
    if starting_position[1] - 1 >= 0 and field[starting_position[0]][starting_position[1] - 1] in ["-", "L", "F"]:
        directions[2] = "1"
    if starting_position[1] - 1 >= 0 and field[starting_position[0]][starting_position[1] + 1] in ["-", "7", "J"]:
        directions[3] = "1"

    return directions_to_field["".join(directions)]

def move(field: list[str], current_position: tuple[int, int],
         last_position: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    new_position: tuple[int, int]
    connecting_positions: tuple[tuple[int, int], tuple[int, int]]

    if field[current_position[0]][current_position[1]] == "|":
        connecting_positions = (
            (current_position[0] + 1, current_position[1]),
            (current_position[0] - 1, current_position[1])
        )
        new_position = (
            connecting_positions[0] if connecting_positions[1] == last_position
            else connecting_positions[1])
    elif field[current_position[0]][current_position[1]] == "-":
        connecting_positions = (
            (current_position[0], current_position[1] + 1),
            (current_position[0], current_position[1] - 1)
        )
        new_position = (
            connecting_positions[0] if connecting_positions[1] == last_position
            else connecting_positions[1])
    elif field[current_position[0]][current_position[1]] == "L":
        connecting_positions = (
            (current_position[0] - 1, current_position[1]),
            (current_position[0], current_position[1] + 1)
        )
        new_position = (
            connecting_positions[0] if connecting_positions[1] == last_position
            else connecting_positions[1])
    elif field[current_position[0]][current_position[1]] == "J":
        connecting_positions = (
            (current_position[0] - 1, current_position[1]),
            (current_position[0], current_position[1] - 1)
        )
        new_position = (
            connecting_positions[0] if connecting_positions[1] == last_position
            else connecting_positions[1])
    elif field[current_position[0]][current_position[1]] == "F":
        connecting_positions = (
            (current_position[0] + 1, current_position[1]),
            (current_position[0], current_position[1] + 1)
        )
        new_position = (
            connecting_positions[0] if connecting_positions[1] == last_position
            else connecting_positions[1])
    elif field[current_position[0]][current_position[1]] == "7":
        connecting_positions = (
            (current_position[0] + 1, current_position[1]),
            (current_position[0], current_position[1] - 1)
        )
        new_position = (
            connecting_positions[0] if connecting_positions[1] == last_position
            else connecting_positions[1])

    return (new_position, current_position)

def steps_to_farthest_point(field: list[str], map_loop: list[list[str]],
                            starting_position: tuple[int, int]) -> int:

    old_position: tuple[int, int] = starting_position
    current_position: tuple[int, int]
    steps: int = 1

    if starting_position[0] - 1 >= 0 and field[starting_position[0] - 1][starting_position[1]] in ["|", "F", "7"]:
        current_position = (starting_position[0] - 1, starting_position[1])
    elif starting_position[0] + 1 < len(field) and field[starting_position[0] + 1][starting_position[1]] in ["|", "L", "J"]:
        current_position = (starting_position[0] + 1, starting_position[1])
    elif starting_position[1] - 1 >= 0 and field[starting_position[0]][starting_position[1] - 1] in ["-", "L", "F"]:
        current_position = (starting_position[0], starting_position[1] - 1)
    else:
        current_position = (starting_position[0], starting_position[1] + 1)

    map_loop[starting_position[0]][starting_position[1]] = get_starting_field(field, starting_position)

    while current_position != starting_position:
        map_loop[current_position[0]][current_position[1]] = field[current_position[0]][current_position[1]]
        current_position, old_position = move(field, current_position, old_position)

        steps += 1

    return int(steps / 2)

def is_inside(position: tuple[int, int], map_loop: list[list[str]]) -> bool:
    if map_loop[position[0]][position[1]] != "0":
        return False

    if not __check_downwards(position, map_loop):
        return False
    if not __check_leftwards(position, map_loop):
        return False
    if not __check_rightwards(position, map_loop):
        return False
    if not __check_upwards(position, map_loop):
        return False

    return True

def __check_upwards(position: tuple[int, int], map_loop: list[list[str]]) -> bool:
    count: int = 0
    number_of_pipes_crossed: int = 0
    move_along_pipe: bool = False
    pipe_start: str
    pipe_crossed: list[str] = ["7L", "L7", "FJ", "JF"]

    if position[0] - 1 >= 0:
        count = 1

        while position[0] - count >= 0:
            if map_loop[position[0] - count][position[1]] == "-":
                number_of_pipes_crossed += 1
            elif map_loop[position[0] - count][position[1]] in ["7", "F", "L", "J"]:
                if move_along_pipe:
                    if pipe_start + map_loop[position[0] - count][position[1]] in pipe_crossed:
                        number_of_pipes_crossed += 1
                    move_along_pipe = False
                else:
                    move_along_pipe = True
                    pipe_start = map_loop[position[0] - count][position[1]]

            count += 1

    if number_of_pipes_crossed % 2 == 0:
        return False

    return True

def __check_downwards(position: tuple[int, int], map_loop: list[list[str]]) -> bool:
    count: int = 0
    number_of_pipes_crossed: int = 0
    move_along_pipe: bool = False
    pipe_start: str
    pipe_crossed: list[str] = ["7L", "L7", "FJ", "JF"]

    if position[0] + 1 < len(map_loop):
        count = 1

        while position[0] + count < len(map_loop):
            if map_loop[position[0] + count][position[1]] == "-":
                number_of_pipes_crossed += 1
            elif map_loop[position[0] + count][position[1]] in ["7", "F", "L", "J"]:
                if move_along_pipe:
                    if pipe_start + map_loop[position[0] + count][position[1]] in pipe_crossed:
                        number_of_pipes_crossed += 1
                    move_along_pipe = False
                else:
                    move_along_pipe = True
                    pipe_start = map_loop[position[0] + count][position[1]]

            count += 1

    if number_of_pipes_crossed % 2 == 0:
        return False

    return True

def __check_rightwards(position: tuple[int, int], map_loop: list[list[str]]) -> bool:
    count: int = 0
    number_of_pipes_crossed: int = 0
    move_along_pipe: bool = False
    pipe_start: str
    pipe_crossed: list[str] = ["7L", "L7", "FJ", "JF"]

    if position[1] - 1 >= 0:
        count = 1

        while position[1] - count >= 0:
            if map_loop[position[0]][position[1] - count] == "|":
                number_of_pipes_crossed += 1
            elif map_loop[position[0]][position[1] - count] in ["7", "F", "L", "J"]:
                if move_along_pipe:
                    if pipe_start + map_loop[position[0]][position[1] - count] in pipe_crossed:
                        number_of_pipes_crossed += 1
                    move_along_pipe = False
                else:
                    move_along_pipe = True
                    pipe_start = map_loop[position[0]][position[1] - count]

            count += 1

    if number_of_pipes_crossed % 2 == 0:
        return False

    return True

def __check_leftwards(position: tuple[int, int], map_loop: list[list[str]]) -> bool:
    count: int = 0
    number_of_pipes_crossed: int = 0
    move_along_pipe: bool = False
    pipe_start: str
    pipe_crossed: list[str] = ["7L", "L7", "FJ", "JF"]

    if position[1] + 1 < len(map_loop[0]):
        count = 1

        while position[1] + count < len(map_loop[0]):
            if map_loop[position[0]][position[1] + count] == "|":
                number_of_pipes_crossed += 1
            elif map_loop[position[0]][position[1] + count] in ["7", "F", "L", "J"]:
                if move_along_pipe:
                    if pipe_start + map_loop[position[0]][position[1] + count] in pipe_crossed:
                        number_of_pipes_crossed += 1
                    move_along_pipe = False
                else:
                    move_along_pipe = True
                    pipe_start = map_loop[position[0]][position[1] + count]

            count += 1

    if number_of_pipes_crossed % 2 == 0:
        return False

    return True

def all_fields_inside(map_loop: list[list[str]]) -> int:
    number_of_fields_inside: int = 0

    for row in range(len(map_loop)):
        for column in range(len(map_loop[0])):
            if is_inside((row, column), map_loop):
                number_of_fields_inside += 1
                map_loop[row][column] = "1"

    return number_of_fields_inside

def main() -> int:
    field = get_input("input.txt")
    map_loop: list[list[str]] = [["0" for _ in range(len(field[0]))] for __ in range(len(field))]
    starting_position: tuple[int, int] = get_starting_position(field)

    # Part 1
    steps: int = steps_to_farthest_point(field, map_loop, starting_position)

    print("Solution Task 1:", steps)

    # Part 2
    number_of_fields_inside: int = all_fields_inside(map_loop)

    print("Solution Task 2", number_of_fields_inside)

if __name__ == "__main__":
    sys.exit(main())
