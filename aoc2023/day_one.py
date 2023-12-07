#!/usr/bin/env python3


def day_one(coordinates: str) -> int:
    lines = parse_coordinates(coordinates)

    numbers_per_lines = list(map(first_last_number_in_line, lines))

    return sum(numbers_per_lines)


def parse_coordinates(text: str) -> list[str]:
    lines = text.split("\n")

    stripped = list(map(lambda line: line.replace(" ", ""), lines))
    non_blank = list(filter(lambda line: line != "", stripped))
    return non_blank


def first_last_number_in_line(line: str) -> int:
    numbers = [char for char in line if char.isdigit()]
    first_number = numbers[0]
    last_number = numbers[-1]
    return int(first_number + last_number)


def run():
    with open('input.txt', 'r') as file:
        content = file.read()
        print(day_one(content))


if __name__ == "__main__":
    run()
