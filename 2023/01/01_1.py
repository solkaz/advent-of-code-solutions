import re

numbers = re.compile(r"^\d$")


def calculate_line(s: str) -> int:
    first: str | None = None
    second: str | None = None
    for char in s:
        if numbers.match(char):
            if first is None:
                first = char
            else:
                second = char
    return int(f"{first}{first}") if second is None else int(f"{first}{second}")


with open("./input.txt", encoding="utf-8") as my_file:
    print(sum(map(calculate_line, my_file)))
