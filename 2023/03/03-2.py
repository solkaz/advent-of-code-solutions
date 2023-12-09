import os
import re

number_group = re.compile(r"\d+")


def calculate_line(lines: (str | None, str, str | None)) -> int:
    prev_line, curr_line, next_line = lines
    current_sum = 0
    for i, char in enumerate(curr_line):
        if char == ".":
            continue
        found_numbers = []
        if not char.isdigit():
            # is a symbol, let's try to find a number around it

            # if a number is on the left
            if i != 0 and curr_line[i - 1].isdigit():
                current_number = ""
                j = i - 1
                while curr_line[j].isdigit() and j >= 0:
                    current_number = curr_line[j] + current_number
                    j -= 1
                found_numbers.append(int(current_number))

            # if a number is on the right
            if i < len(curr_line) - 1 and curr_line[i + 1].isdigit():
                current_number = ""
                j = i + 1
                while j < len(curr_line) and curr_line[j].isdigit():
                    current_number += curr_line[j]
                    j += 1
                found_numbers.append(int(current_number))

            # check the row above, if applicable
            if prev_line is not None:
                upper = prev_line[i]
                j = i - 1
                while j >= 0 and prev_line[j].isdigit():
                    upper = prev_line[j] + upper
                    j -= 1

                j = i + 1
                while j < len(prev_line) and prev_line[j].isdigit():
                    upper += prev_line[j]
                    j += 1

                for number in number_group.findall(upper):
                    found_numbers.append(int(number))

            if next_line is not None:
                lower = next_line[i]
                j = i - 1
                while j >= 0 and next_line[j].isdigit():
                    lower = next_line[j] + lower
                    j -= 1

                j = i + 1
                while j < len(next_line) and next_line[j].isdigit():
                    lower += next_line[j]
                    j += 1

                for number in number_group.findall(lower):
                    found_numbers.append(int(number))

        if len(found_numbers) == 2:
            current_sum += found_numbers[0] * found_numbers[1]
    return current_sum


def create_tuples(file):
    lines = list(map(str.rstrip, file))
    result = []
    for i, line in enumerate(lines):
        prev_line = lines[i - 1] if i - 1 >= 0 else None
        curr_line = line
        next_line = lines[i + 1] if i + 1 < len(lines) else None
        result.append((prev_line, curr_line, next_line))
    return result


with open(f"{os.path.dirname(__file__)}/input.txt", encoding="utf-8") as my_file:
    print(sum(map(calculate_line, create_tuples(my_file))))
