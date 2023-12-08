import sys

def get_input(path_to_input: str) -> list[str]:   
    with open(path_to_input) as input:
        input: list[str] = input.read().splitlines()

    return input

def check_cards(cards: str, check_jokers: bool) -> str:
    labels: list[str] = []
    label_count: list[int] = []

    if check_jokers:
        number_of_jokers: int = 0

    for card in [*cards]:
        if card in labels:
            label_count[labels.index(card)] += 1
        elif check_jokers and card == "J":
            number_of_jokers += 1
        else:
            labels.append(card)
            label_count.append(1)

    if check_jokers and number_of_jokers > 0:
        if len(labels) == 1 or number_of_jokers == 5:
            return "Five kind"
        if number_of_jokers == 1:
            if len(labels) == 4:
                return "One pair"
            if len(labels) == 3:
                return "Three kind"
            if 3 in label_count:
                return "Four kind"
            return "Full house"
        elif number_of_jokers == 2:
            if len(labels) == 3:
                return "Three kind"
            return "Four kind"
        else:
            return "Four kind"
    else:
        if len(labels) == 1:
            return "Five kind"
        if 4 in label_count:
            return "Four kind"
        if 2 in label_count and 3 in label_count:
            return "Full house"
        if 3 in label_count:
            return "Three kind"
        if label_count.count(2) == 2:
            return "Two pair"
        if 2 in label_count:
            return "One pair"
        return "High card"

def sort_cards_by_type(cards: list[str],
                       check_jokers: bool) -> list[list[tuple[str, int]]]:
    # Length of 7 because there are 7 different kinds of hands
    cards_and_bits: list[list[tuple[str, int]]] = [[] for _ in range(7)]
    type_to_index: dict[str, int] = {
        "Five kind": 0, "Four kind": 1, "Full house": 2, "Three kind": 3,
        "Two pair": 4, "One pair": 5, "High card": 6}

    for card in cards:
        hand: str = card.split()[0]
        bid: int = int(card.split()[1])

        hand_type: str = check_cards(hand, check_jokers)
        index = type_to_index[hand_type]

        cards_and_bits[index].append((hand, bid))

    return cards_and_bits

def sort_cards_by_order(cards_and_bits: list[list[tuple[str, int]]],
                        check_jokers: bool) -> list[tuple[str, int]]:
    hands_ordered: list[tuple[str, int]] = []
    card_to_index: dict[str, int] = {
        "A": 0, "K": 1, "Q": 2, "T": 3, "9": 4, "8": 5, "7": 6, "6": 7, "5": 8,
        "4": 9, "3": 10, "2": 11, "J": 12
        } if check_jokers else {
            "A": 0, "K": 1, "Q": 2, "J": 3, "T": 4, "9": 5, "8": 6, "7": 7, "6": 8,
            "5": 9, "4": 10, "3": 11, "2": 12}


    for label in cards_and_bits:
        label_copy = label.copy()

        for i in range(4, -1, -1):
            hand_sorted_by_card = [[] for _ in range(13)]

            for hand in label_copy:
                index = card_to_index[hand[0][i]]
                hand_sorted_by_card[index].append(hand)

            label_copy = sum(hand_sorted_by_card, [])

        hands_ordered.append(label_copy)

    return sum(hands_ordered, [])

def calculate_winnings(hands_ordered: list[tuple[str, int]]) -> int:
    number_of_hands: int = len(hands_ordered)
    total_winnings: int = 0

    for number, hand in enumerate(hands_ordered):
        total_winnings += (number_of_hands - number) * hand[1]

    return total_winnings

def main() -> int:
    cards: list[str] = get_input("input.txt")

    # Part 1
    cards_and_bits: list[list[tuple[str, int]]] = sort_cards_by_type(cards, False)
    hands_ordered: list[tuple[str, int]] = sort_cards_by_order(cards_and_bits, False)
    total_winnings: int = calculate_winnings(hands_ordered)

    print("Solution Task 1:", total_winnings)

    # Part 2
    cards_and_bits: list[list[tuple[str, int]]] = sort_cards_by_type(cards, True)
    hands_ordered: list[tuple[str, int]] = sort_cards_by_order(cards_and_bits, True)
    total_winnings: int = calculate_winnings(hands_ordered)

    print("Solution Task 2:", total_winnings)

    return 0

if __name__ == "__main__":
    sys.exit(main())