import re

game_number_regex = re.compile(r"^Game (\d+):")
blue_cubes_regex = re.compile(r"(\d+) blue")
red_cubes_regex = re.compile(r"(\d+) red")
green_cubes_regex = re.compile(r"(\d+) green")

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14


def calculate_line(s: str) -> int:
    game_number = game_number_regex.match(s).group(1)

    for regex in [blue_cubes_regex, red_cubes_regex, green_cubes_regex]:
        if len([i for i in regex.findall(s) if int(i) > MAX_BLUE_CUBES]) != 0:
            return 0
    return int(game_number)


with open("./input.txt") as my_file:
    print(sum(map(calculate_line, my_file)))
