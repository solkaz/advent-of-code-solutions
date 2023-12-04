import re

blue_cubes_regex = re.compile(r"(\d+) blue")
red_cubes_regex = re.compile(r"(\d+) red")
green_cubes_regex = re.compile(r"(\d+) green")


def calculate_line(s: str) -> int:
    blue_cubes_results = blue_cubes_regex.findall(s)
    min_blue_cubes = max(int(i) for i in blue_cubes_results)

    red_cubes_results = red_cubes_regex.findall(s)
    min_red_cubes = max(int(i) for i in red_cubes_results)

    green_cubes_results = green_cubes_regex.findall(s)
    min_green_cubes = max(int(i) for i in green_cubes_results)

    return min_blue_cubes * min_red_cubes * min_green_cubes


with open("./input.txt") as my_file:
    print(sum(map(calculate_line, my_file)))
