import sys

from operator import itemgetter

def get_input(path_to_input: str) -> tuple[list[list[int]]]:
  with open(path_to_input) as input:
    result = tuple(
        sorted(([int(num) for num in lines.split()]
                for lines in part.split(':')[1].strip().split('\n')),
               key=itemgetter(1)) for part in input.read().split('\n\n'))

    for trans in result[1:]:
      for item in trans:
        dest: int
        source: int
        step: int
        dest, source, step = item

        item[0] = source
        item[1] = source + step
        item[2] = dest - source

    return result

def find_location(seeds: list[list[int]], data: tuple[list[list[int]]]) -> int:
    for trans in data:
        new_seeds: list[list[int]] = []

        for seed in seeds:
            for start, finish, move in trans:
                if seed[0] < start:
                    if seed[1] <= start:
                        new_seeds.append(seed)
                        seed = 0
                        break
                    else:
                        new_seeds.append([seed[0], start])
                        seed[0] = start

                if start <= seed[0] < finish:
                    new_seeds.append([seed[0] + move, min(seed[1], finish) + move])

                    if seed[1] <= finish:
                        seed = 0
                        break
                    else:
                        seed[0] = finish

            if seed:
                new_seeds.append(seed)

            seeds = new_seeds

    return min(seeds)[0]

def main() -> int:
    almanac = get_input("input.txt")

    # Part 1
    seeds = [[num, num + 1] for num in almanac[0][0]]
    lowest_location_number = find_location(seeds, almanac[1:])

    print("Solution Task 1:", lowest_location_number)

    # Part 2
    seeds = almanac[0][0]
    seeds = [[seeds[num], seeds[num] + seeds[num + 1]]
             for num in range(0, len(seeds) - 1, 2)]
    lowest_location_number = find_location(seeds, almanac[1:])

    print("Solution Task 1:", lowest_location_number)

    return 0

if __name__ == "__main__":
    sys.exit(main())
