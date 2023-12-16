import sys

def get_input(path_to_input: str) -> list[str]:   
    with open(path_to_input) as input:
        input: list[str] = input.read().splitlines()[0].split(",")

    return input

def hash_algorithm(sequence: str) -> int:
    number: int = 0

    for char in sequence:
        number = (number + ord(char)) * 17 % 256

    return number

def hash_sequences(sequences: list[str]):
    sum_hash_values: int = 0

    for sequence in sequences:
        sum_hash_values += hash_algorithm(sequence)

    return sum_hash_values

def pack_boxes(sequences: list[str]) -> list[list[str]]:
    packed_boxes: list[list[str]] = [[] for _ in range(256)]

    for sequence in sequences:
        if "=" in sequence:
            split_sequece: list[str] = sequence.split("=")
            box_number = hash_algorithm(split_sequece[0])
            replaced: bool = False

            for label in range(len(packed_boxes[box_number])):
                if split_sequece[0] in packed_boxes[box_number][label]:
                    packed_boxes[box_number][label] = "".join(split_sequece)
                    replaced = True

            if not replaced:
                packed_boxes[box_number].append("".join(split_sequece))
        else:
            box_number: int = hash_algorithm(sequence[:-1])

            for label in range(len(packed_boxes[box_number])):
                if sequence[:-1] == packed_boxes[box_number][label][:-1]:
                    del(packed_boxes[box_number][label])
                    break

    return packed_boxes

def calculate_focusing_power(packed_boxes: list[list[str]]) -> int:
    focusing_power: int = 0

    for box_number, box in enumerate(packed_boxes):
        for lens_number, lens in enumerate(box):
            focusing_power += (1 + box_number) * (1 + lens_number) * int(lens[len(lens) - 1])

    return focusing_power

def main() -> int:
    sequences: list[str] = get_input("input.txt")

    # Part 1
    sum_hash_values: int = hash_sequences(sequences)

    print("Solution Task 1:", sum_hash_values)

    # Part 2
    packed_boxes: list[list[str]] = pack_boxes(sequences)
    focusing_power: int = calculate_focusing_power(packed_boxes)

    print("Solution Part 2:", focusing_power)

    return 0

if __name__ == "__main__":
    sys.exit(main())
