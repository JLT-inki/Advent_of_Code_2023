import sys

NUMBER_AS_WORDS: dict[str, str] = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
    "seven": "7", "eight": "8","nine": "9"}

def get_input(path_to_input: str) -> list[str]:   
    with open(path_to_input) as input:
        input: list[str] = input.read().splitlines()

    return input

def calculate_calibration_value_digits(lines: list[str]) -> int:
    calibration_value: int = 0

    for line in lines:
        for letter in line:
            if letter.isnumeric():
                first_number: str = letter
                break

        for letter in reversed(line):
            if letter.isnumeric():
                last_number: str = letter
                break

        calibration_value += int(first_number + last_number)

    return calibration_value

def calculate_true_calibration_value(lines: list[str]) -> int:
    calibration_value: int = 0

    for line in lines:
        first_number: str
        last_number: str

        for i in range(len(line)):
            if line[i].isnumeric():
                if first_number == "":
                    first_number = line[i]
                else:
                    last_number = line[i]
            elif len(line[i:]) > 4:
                line_copy: str = line[i:]

                for number in NUMBER_AS_WORDS:
                    if number in line_copy[:i+5]:
                        if first_number == "":
                            for j in range(len(line_copy[:i+5])):
                                if line_copy[j].isnumeric():
                                    first_number = line_copy[j]
                                    break

                                if number not in line_copy[:i+5][j:]:
                                    first_number = NUMBER_AS_WORDS[number]
                                    break
                        else:
                            last_number = NUMBER_AS_WORDS[number]

                        break
            elif len(line[i:]) > 3:
                line_copy: str = line[i:]

                for number in NUMBER_AS_WORDS:
                    if number in line_copy[:i+4]:
                        if first_number == "":
                            for j in range(len(line_copy[:i+4])):
                                if line_copy[j].isnumeric():
                                    first_number = line_copy[j]
                                    break

                                if number not in line_copy[:i+4][j:]:
                                    first_number = NUMBER_AS_WORDS[number]
                                    break
                        else:
                            last_number = NUMBER_AS_WORDS[number]

                        break
            elif len(line[i:]) > 2:
                line_copy: str = line[i:]

                for number in NUMBER_AS_WORDS:
                    if number in line_copy[:i+3]:
                        if first_number == "":
                            for j in range(len(line_copy[:i+3])):
                                if line_copy[j].isnumeric():
                                    first_number = line_copy[j]
                                    break

                                if number not in line_copy[:i+3][j:]:
                                    first_number = NUMBER_AS_WORDS[number]
                                    break
                        else:
                            last_number = NUMBER_AS_WORDS[number]

                        break

        if last_number == "":
            last_number = first_number             
        calibration_value += int(first_number + last_number)

    return calibration_value

def main() -> int:
    lines: list[str] = get_input("input.txt")

    calibration_value_1: int = calculate_calibration_value_digits(lines)
    calibration_value_2: int = calculate_calibration_value_digits(lines)

    print("Solution Task 1:", calibration_value_1)
    print("Solution Task 2:", calibration_value_2)

    return 0

if __name__ == "__main__":
    sys.exit(main())
