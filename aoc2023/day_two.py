#!/usr/bin/env python3


def day_two(games: str) -> int:
    return 1


def parse_games(games: str) -> list[str]:
    return games.split('\n')


def run():
    with open('day_two.txt', 'r') as file:
        content = file.read()
        print(day_two(content))


if __name__ == "__main__":
    run()
