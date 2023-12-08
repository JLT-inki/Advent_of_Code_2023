import sys

def get_input(path_to_input: str) -> list[str]:   
    with open(path_to_input) as input:
        input: list[str] = input.read().splitlines()

    return input

def get_number_of_points_and_cards(cards: list[str]) -> tuple[int, int]:
    points_total: int = 0
    number_of_cards: list[int] = [1 for _ in range(len(cards))]

    for card_number, card in enumerate(cards):
        winning_numbers: list[str] = card.split(" | ")[0].split()
        your_numbers: list[str] = card.split(" | ")[1].split()
        number_of_wins: int = 0

        for number in winning_numbers:
            if number in your_numbers:
                number_of_wins += 1

        if number_of_wins > 0:
            points_total += 2 ** (number_of_wins - 1)

        for j in range(1, number_of_wins + 1):
            number_of_cards[card_number + j] += 1 * number_of_cards[card_number]

    return (points_total, sum(number_of_cards))

def main() -> int:
    cards: list[str] = get_input("input.txt")

    points_total: int
    total_scratch_cards: int
    points_total, total_scratch_cards = get_number_of_points_and_cards(cards)

    print("Solution Task 1:", points_total)
    print("Solution Task 2:", total_scratch_cards)

    return 0

if __name__ == "__main__":
    sys.exit(main())
