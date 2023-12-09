ticket_number_count = {}


def parse_numbers_list(s: str) -> list[int]:
    return [int(i) for i in s.split(" ") if i.strip() != ""]


def calculate_line(s: str, current_line: int) -> int:
    winning_numbers, card_numbers = map(
        parse_numbers_list, s.strip().split(": ")[1].split(" | ")
    )
    score = 0
    for number in card_numbers:
        if number in winning_numbers:
            score += 1

    number_of_tickets_for_current_line = ticket_number_count.get(current_line, 0)
    for x in range(current_line + 1, score + current_line + 1):
        ticket_number_count[x] = ticket_number_count.get(x, 0) + (
            number_of_tickets_for_current_line + 1
        )
    return 1 + ticket_number_count.get(current_line, 0)


with open("./input.txt", encoding="utf-8") as my_file:
    line_count = 1
    answer = 0
    for line in my_file:
        answer += calculate_line(line, line_count)
        line_count += 1
    print(answer)
