def parse_numbers_list(s: str) -> list[int]:
    return [int(i) for i in s.split(" ") if i.strip() != ""]


def calculate_line(s: str) -> int:
    winning_numbers, card_numbers = map(
        parse_numbers_list, s.strip().split(": ")[1].split(" | ")
    )
    score = 0
    for number in card_numbers:
        if number in winning_numbers:
            score = 1 if score == 0 else score * 2
    return score


with open("./input.txt", encoding="utf-8") as my_file:
    print(sum(map(calculate_line, my_file)))
