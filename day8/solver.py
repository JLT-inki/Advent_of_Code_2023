import sys

def get_input(path_to_input: str) -> list[str]:   
    with open(path_to_input) as input:
        input: list[str] = input.read().splitlines()

    return input

def get_sequence(input: str) -> str:
    return input[0]

def get_network(input: str) -> list[list[str]]:
    network: list[tuple[str, str, str]] = []

    for line_number, line in enumerate(input[2:]):
        network.append([])
        element: str = ""

        for char in [*line]:
            if char.isalpha():
                element += char
            else:
                if element == "":
                    continue
                network[line_number].append(element)
                element = ""

    return network

def find_index_of_position(network: list[list[str]], position: str) -> int:
    for idx, node in enumerate(network):
        if node[0] == position:
            return idx

def find_all_starting_points(network: list[list[str]]) -> list[int]:
    starting_positions: list[int] = []

    for idx, node in enumerate(network):
        if node[0][2] == "A":
            starting_positions.append(idx)

    return starting_positions

def move_sequence(sequence: str, network: list[list[str]],
                  index_current_position: int) -> int:
    for movement in sequence:
        if movement == "L":
            new_position = network[index_current_position][1]
        else:
            new_position = network[index_current_position][2]

        index_current_position = find_index_of_position(network, new_position)

    return index_current_position

def main() -> int:
    input: list[str] = get_input('./input.txt')
    sequence: str = get_sequence(input)
    network: list[list[str]] = get_network(input)

    # Part 1
    idx: int = find_index_of_position(network, "AAA")
    count: int = 0

    while network[idx][0] != "ZZZ":
        idx = move_sequence(sequence, network, idx)
        count += 1

    print("Solution Task 1:", count * len(sequence))

    # Part 2
    starting_positions: list[int] = find_all_starting_points(network)
    cycles:list[int] = []

    for position in starting_positions:
        count = 0
        idx = position

        while network[idx][0][2] != "Z":
            idx = move_sequence(sequence, network, idx)
            count += 1

        cycles.append(count)

    ending_point: int = cycles[0]

    for cycle in cycles[1:]:
        ending_point_tmp = ending_point

        while ending_point % cycle != 0:
            ending_point += ending_point_tmp

    print("Solution Task 2:", ending_point * len(sequence))
    return 0

if __name__ == "__main__":
    sys.exit(main())
