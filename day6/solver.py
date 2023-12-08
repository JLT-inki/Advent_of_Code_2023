import sys

def get_input(path_to_input: str) -> list[list[str]]:   
    with open(path_to_input) as input:
        input: list[list[str]] = [
            line.split(":")[1].split() for line in input.read().splitlines()]

    return input

def beat_record(input: list[list[str]], one_race: bool) -> int:
    if one_race:
        number_of_possibilities: int = 0
        time_and_distance: tuple[int, int] = (
            int("".join(input[0])), int("".join(input[1])))

        for speed in range(time_and_distance[0] + 1):
            remaining_time: int = time_and_distance[0] - speed

            if speed * remaining_time > time_and_distance[1]:
                number_of_possibilities += 1
            elif number_of_possibilities > 0:
                break
    else:
        number_of_possibilities: int = 1
        time_and_distances: list[tuple[int, int]] = [
            (int(input[0][i]), int(input[1][i])) for i in range(len(input[0]))]

        for race in time_and_distances:
            time: int = race[0]
            distance: int = race[1]
            number_of_wins: int = 0

            for speed in range(time + 1):
                remaining_time: int = time - speed

                if speed * remaining_time > distance:
                    number_of_wins += 1

            if number_of_wins > 0:
                number_of_possibilities *= number_of_wins


    return number_of_possibilities

def main() -> int:
    input: list[str] = get_input("input.txt")

    total_number_of_wins: int = beat_record(input, False)
    total_number_of_wins_2: int = beat_record(input, True)

    print("Solution Task 1:", total_number_of_wins)
    print("Solution Task 1:", total_number_of_wins_2)

    return 0

if __name__ == "__main__":
    sys.exit(main())
