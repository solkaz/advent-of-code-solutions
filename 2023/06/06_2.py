from typing import Tuple
from math import ceil, floor, sqrt


def parse_number_from_line(s: str) -> int:
    return int("".join(s.strip().split(": ")[1].split(" ")))


def multiply(a, b):
    return a * b


# Inspired by https://github.com/mahakaal/adventofcode/blob/main/2023/day06/day06.go
def process_time_distance_pair(time_distance_pair: Tuple[int, int]) -> int:
    time, distance = time_distance_pair
    delta = sqrt(time**2 - (4 * distance))
    min_val = (float(time) - delta) / 2
    max_val = (float(time) + delta) / 2

    if min_val - float(int(min_val)) == 0:
        min_val += 1
    else:
        min_val = ceil(min_val)

    if max_val - float(int(max_val)) == 0:
        max_val -= 1
    else:
        max_val = floor(max_val)
    return int(max_val - min_val) + 1


with open("./input.txt", encoding="utf-8") as my_file:
    time_distance_pairs = (
        parse_number_from_line(my_file.readline()),
        parse_number_from_line(my_file.readline()),
    )
    print(process_time_distance_pair(time_distance_pairs))
