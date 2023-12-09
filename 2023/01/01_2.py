import re

numbers = re.compile(r"^\d$")

NUMBERS_MAP = {
    "zerone": "01",
    "twone": "21",
    "eightwo": "82",
    "eighthree": "83",
    "oneight": "18",
    "threeight": "38",
    "fiveight": "58",
    "nineight": "98",
    "sevenine": "79",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def calculate_line(line: str) -> int:
    for [number_as_word, number_as_numeric] in NUMBERS_MAP.items():
        line = line.replace(number_as_word, number_as_numeric)
    first: str | None = None
    second: str | None = None
    for char in line:
        if numbers.match(char):
            if first is None:
                first = char
            else:
                second = char
    return int(f"{first}{first}") if second is None else int(f"{first}{second}")


with open("./input.txt", encoding="utf-8") as my_file:
    print(sum(map(calculate_line, my_file)))
