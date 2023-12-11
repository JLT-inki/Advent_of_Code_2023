import sys

def get_input(path_to_input: str) -> list[list[int]]:   
    with open(path_to_input) as input:
        input: list[list[int]] = [[
            int(number) for number in line.split()
            ] for line in input.read().splitlines()]

    return input

def get_next_sequence(sequence: list[int]) -> list[int]:
    next_sequence: list[int] = []

    for i in range(len(sequence) - 1):
        next_sequence.append(sequence[i + 1] - sequence[i])

    return next_sequence

def find_all_sequences(line: list[int]) -> list[list[int]]:
    all_sequences: list[list[int]] = [line]

    while not all(number == 0 for number in all_sequences[len(all_sequences) - 1]):
        all_sequences.append(get_next_sequence(all_sequences[len(all_sequences) - 1]))

    return all_sequences

def extrapolate(sequences: list[list[int]]) -> int:
    current_line: int = len(sequences) - 1
    current_index: int = len(sequences[current_line])

    sequences[current_line].append(0)

    while current_line > 0:
        sequences[current_line - 1].append(sequences[current_line - 1][current_index]
                                           + sequences[current_line][current_index])
        current_line -= 1
        current_index += 1

    return sequences[current_line][current_index]

def extrapolate_backwards(sequences: list[list[int]]) -> int:
    current_line: int = len(sequences) - 1

    sequences[current_line].insert(0, 0)

    while current_line > 0:
        sequences[current_line - 1].insert(0, sequences[current_line - 1][0]
                                           - sequences[current_line][0])

        current_line -= 1

    return sequences[0][0]

def main() -> int:
    starting_sequences: list[list[int]] = get_input("input.txt")

    next_numbers: list[int] = []
    first_numbers: list[int] = []

    for sequence in starting_sequences:
        all_sequences: list[list[int]] = find_all_sequences(sequence)

        next_numbers.append(extrapolate(all_sequences))
        first_numbers.append(extrapolate_backwards(all_sequences))

    print("Solution task 1:", sum(next_numbers))
    print("Solution task 2:", sum(first_numbers))

    return 0

if __name__ == "__main__":
    sys.exit(main())
