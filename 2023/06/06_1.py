from functools import reduce
from typing import Tuple


def parse_numbers_list(s: str) -> list[int]:
    return [int(i) for i in s.strip().split(": ")[1].split(" ") if i.strip() != ""]


def multiply(a, b):
    return a * b


def process_time_distance_pair(time_distance_pair: Tuple[int, int]) -> int:
    time, distance = time_distance_pair
    number_of_times_to_hold_button = 0
    for time_to_hold_button in range(1, time):
        time_to_run = time - time_to_hold_button
        distance_ran = time_to_run * time_to_hold_button
        if distance_ran > distance:
            number_of_times_to_hold_button += 1

    return number_of_times_to_hold_button


with open("./input.txt", encoding="utf-8") as my_file:
    time_distance_pairs = list(
        zip(
            parse_numbers_list(my_file.readline()),
            parse_numbers_list(my_file.readline()),
        )
    )
    print(reduce(multiply, map(process_time_distance_pair, time_distance_pairs)))
