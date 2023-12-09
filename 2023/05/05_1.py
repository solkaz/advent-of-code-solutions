import os
import re
from typing import Tuple

number = re.compile(r"\d")


def apply_map(sources: list[int], translators: list[Tuple[int, int, int]]):
    destinations: list[int] = []
    for source in sources:
        destination = source
        for translator in translators:
            dest_start, source_start, translator_range = translator
            if source in range(source_start, source_start + translator_range):
                destination = source + (dest_start - source_start)
        destinations.append(destination)

    return destinations


with open(f"{os.path.dirname(__file__)}/input.txt", encoding="utf-8") as my_file:
    lines = [line for line in my_file.readlines() if line.strip() != ""]
    seeds = [int(i) for i in lines[0].strip().split(": ")[1].split(" ")]
    current_map: list[Tuple[int, int, int]] | None = None
    for i, line in enumerate(lines):
        if not number.match(line):
            if current_map is None:
                current_map = []
            else:
                seeds = apply_map(seeds, current_map)
                current_map = []

        else:
            current_map.append(tuple(int(i) for i in line.strip().split(" ")))

    print(min(apply_map(seeds, current_map)))
