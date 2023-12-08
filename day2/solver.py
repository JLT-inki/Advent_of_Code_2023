import sys

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def get_input(path_to_input: str) -> list[str]:   
    with open(path_to_input) as input:
        input: list[str] = input.read().splitlines()

    return input

def play_games(games: list[str]) -> tuple[int, int]:
    sum_games_possible: int = 0
    power_cubes: int = 0

    for id, game in enumerate(games):
        game_copy: list[str] = game.split(": ")[1].split("; ")
        game_possible: bool = True

        blue_balls: int = 0
        red_balls: int = 0
        green_balls: int = 0
        
        for set in game_copy:
            set_tmp: list[str] = set.split(", ")

            for balls in set_tmp:
                if "blue" in balls:
                    balls: int = int(balls.split()[0])

                    if balls > MAX_BLUE:
                        game_possible = False

                    if balls > blue_balls:
                        blue_balls = balls
                elif "red" in balls:
                    balls: int = int(balls.split()[0])

                    if balls > MAX_RED:
                        game_possible = False

                    if balls > red_balls:
                        red_balls = balls
                else:
                    balls: int = int(balls.split()[0])

                    if balls > MAX_GREEN:
                        game_possible = False

                    if balls > green_balls:
                        green_balls = balls
        
        if game_possible:
            sum_games_possible += 1 + id

        power_cubes += blue_balls * red_balls * green_balls

    return (sum_games_possible, power_cubes)

def main() -> int:
    games: list[str] = get_input('input.txt')

    sum_games_possible: int
    power_cubes: int
    sum_games_possible, power_cubes = play_games(games)

    print("Solution Task 1:", sum_games_possible)
    print("Solution Task 2:", power_cubes)

    return 0

if __name__ == "__main__":
    sys.exit(main())