import sys

def get_input(path_to_input: str) -> list[str]:   
    with open(path_to_input) as input:
        input: list[str] = input.read().splitlines()

    return input

def get_individual_fields(fields: list[str]) -> list[list[str]]:
    individual_fields: list[list[str]] = [[]]
    count: int = 0

    for line in fields:
        if line == "":
            individual_fields.append([])
            count += 1
        else:
            individual_fields[count].append(line)

    return individual_fields

def split_field_vertically(field: list[str],
                           split_after: int) -> tuple[list[str], list[str]]:
    left_split: list[str] = []
    right_split: list[str] = []

    for count_line, line in enumerate(field):
        left_split.append("")
        right_split.append("")

        for count, char in enumerate(line):
            if count < split_after:
                left_split[count_line] += char
            else:
                right_split[count_line] += char

    return left_split, right_split

def split_field_horizontally(field: list[str],
                             split_after: int) -> tuple[list[str], list[str]]:
    upper_split: list[str] = []
    lower_split: list[str] = []

    for count, line in enumerate(field):
        if count < split_after:
            upper_split.append(line)
        else:
            lower_split.append(line)

    return (upper_split, lower_split)

def check_split_vertically(left_split: list[str], right_split: list[str],
                           part_2: bool) -> bool:
    if part_2:
        number_of_smudges: int = 0

    for line_left, line_right in zip(left_split, right_split):
        for char_left, char_right in zip(reversed(line_left), line_right):
            if char_left != char_right:
                if not part_2 or number_of_smudges != 0:
                    return False
                number_of_smudges = 1

    if not part_2 or number_of_smudges == 1:
        return True
    return False

def check_split_horizontally(upper_split: list[str], lower_split: list[str],
                             part_2: bool) -> bool:
    if part_2:
        number_of_smudges: int = 0
    for upper_line, lower_line in zip(reversed(upper_split), lower_split):
        for char_upper, char_lower in zip(upper_line, lower_line):
            if char_upper != char_lower:
                if not part_2 or number_of_smudges != 0:
                    return False
                number_of_smudges = 1

    if not part_2 or number_of_smudges == 1:
        return True
    return False

def summarize_notes(individual_fields: list[list[str]], part_2: bool) -> int:
    sum_notes: int = 0

    for field in individual_fields:
        value_note: int = 0

        left_split: list[str]
        right_split: list[str]

        for split_after in range(len(field[0]) - 1):
            left_split, right_split = split_field_vertically(field, split_after + 1)

            if check_split_vertically(left_split, right_split, part_2):
                value_note = split_after + 1
                break

        if value_note > 0:
            sum_notes += value_note
            continue

        upper_split: list[str]
        lower_split: list[str]

        for split_after in range(len(field) - 1):
            upper_split, lower_split = split_field_horizontally(field, split_after + 1)

            if check_split_horizontally(upper_split, lower_split, part_2):
                value_note = 100 * (split_after + 1)
                break

        sum_notes += value_note

    return sum_notes

def main() -> int:
    fields: list[str] = get_input("input.txt")
    individual_fields: list[list[str]] = get_individual_fields(fields)

    # Part 1
    sum_notes_part_1: int = summarize_notes(individual_fields, False)

    print("Solution Task 1:", sum_notes_part_1)

    # Part 2
    sum_notes_part_2: int = summarize_notes(individual_fields, True)

    print("Solution Task 2:", sum_notes_part_2)

    return 0

if __name__ == "__main__":
    sys.exit(main())
