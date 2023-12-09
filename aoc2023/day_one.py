#!/usr/bin/env python3


def day_one(coordinates: str) -> int:
    lines = parse_coordinates(coordinates)

    words_as_nums = list(map(replace_words_with_nums, lines))
    numbers_per_lines = list(map(first_last_number_in_line, words_as_nums))

    return sum(numbers_per_lines)


def replace_words_with_nums(words: str) -> str:
    words_to_nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    line = ""
    for char in words:
        line += char
        for word, num in words_to_nums.items():
            if word in line:
                line = line.replace(word, num)
    return line


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
    with open('day_one.txt', 'r') as file:
        content = file.read()
        print(day_one(content))


if __name__ == "__main__":
    run()
