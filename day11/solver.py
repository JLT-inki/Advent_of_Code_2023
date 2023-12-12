import sys

def get_input(path_to_input: str) -> list[str]:   
    with open(path_to_input) as input:
        input: list[str] = input.read().splitlines()

    return input

def find_expansions(image: list[str]) -> tuple[list[int], list[int]]:
    colums_expanded: list[int] = []
    rows_expanded: list[int] = []

    image_expanded: list[str] = []

    for row_number, row in enumerate(image):
        if row.count(".") == len(row):
            rows_expanded.append(row_number)

    for col_number in range(len(image[0])):
        column: str = "".join([
            image[row][col_number] for row in range(len(image))])

        if column.count(".") == len(column):
            colums_expanded.append(col_number)

    for row in range(len(image)):
        if row in rows_expanded:
            image_expanded.append([
                "." for _ in range(len(image[0]) + len(colums_expanded))])
        image_expanded.append([])

        for column in range(len(image[0])):
            if column in colums_expanded:
                image_expanded[len(image_expanded) - 1].append(".")
            image_expanded[len(image_expanded) - 1].append(image[row][column])

    return rows_expanded, colums_expanded

def get_all_galaxy_positions(image: list[str], rows_expanded: list[int],
                             colums_expanded: list[int], expansion_factor: int
                             ) -> list[tuple[int, int]]:
    galaxy_positions: list[tuple[int, int]] = []

    for row in range(len(image)):
        for column in range(len(image[0])):
            if image[row][column] == "#":
                expansion_factor_row: int = -1
                expansion_factor_column: int = -1

                for count, expanded_row in enumerate(rows_expanded):
                    if expanded_row > row:
                        expansion_factor_row = count
                        break

                for count, expanded_column in enumerate(colums_expanded):
                    if expanded_column > column:
                        expansion_factor_column = count
                        break

                if expansion_factor_column == -1:
                    expansion_factor_column = len(colums_expanded)
                if expansion_factor_row == -1:
                    expansion_factor_row = len(rows_expanded)

                galaxy_positions.append((
                    row + expansion_factor_row * expansion_factor,
                    column + expansion_factor_column * expansion_factor))

    return galaxy_positions

def calculate_all_distances(galaxy_positions: list[tuple[int, int]]) -> int:
    sum_distances: int = 0

    for number, galaxy_1 in enumerate(galaxy_positions):
        for galaxy_2 in galaxy_positions[:number]:
            sum_distances += (
                abs(galaxy_1[0] - galaxy_2[0]) + abs(galaxy_1[1] - galaxy_2[1]))

    return sum_distances

def main() -> int:
    image: list[str] = get_input("input.txt")

    rows_expanded: list[int]
    colums_expanded: list[int]
    rows_expanded, colums_expanded = find_expansions(image)

    # Part 1
    galaxy_positions_1: list[tuple[int, int]] = get_all_galaxy_positions(image, rows_expanded, colums_expanded, 1)
    distances_part_1: int = calculate_all_distances(galaxy_positions_1)

    print("Solution Task 1:", distances_part_1)

    # Part 2
    galaxy_positions_2: list[tuple[int, int]] = get_all_galaxy_positions(image, rows_expanded, colums_expanded, 999999)
    distances_part_2: int = calculate_all_distances(galaxy_positions_2)

    print("Solution Task 2:", distances_part_2)

    return 0

if __name__ == "__main__":
    sys.exit(main())
