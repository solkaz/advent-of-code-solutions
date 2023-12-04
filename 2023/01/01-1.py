import re

numbers = re.compile(r"^\d$")


def calculate_line(s: str) -> int:
    first: int | None = None
    second: int | None = None
    for char in s:
        if numbers.match(char):
            if first is None:
                first = char
            else:
                second = char
    if second is None:
        return int(f"{first}{first}")
    else:
        return int(f"{first}{second}")


with open("./input.txt", encoding="utf-8") as my_file:
    print(sum(map(calculate_line, my_file)))
