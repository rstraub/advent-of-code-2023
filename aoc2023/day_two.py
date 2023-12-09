#!/usr/bin/env python3
from typing import List, Dict, Any


def day_two(games: str) -> int:
    return 1


def parse_games(games: str) -> list[dict[str, int]]:
    lines: list[str] = games.split('\n')

    result = []
    for line in lines:
        game, sets = line.split(': ')

        result.append({
            'id': parse_game_id(game),
            'sets': parse_sets(sets)
        })

    return result


def parse_sets(sets: str) -> list[dict[str, int]]:
    result = []
    for a_set in sets.split('; '):
        result.append(parse_set(a_set))

    return result


def parse_set(a_set: str) -> dict[str, int]:
    result = {}
    for item in a_set.split(', '):
        count, color = item.split(' ')
        result[color] = int(count)

    return result

def parse_game_id(game: str) -> int:
    return int(game.split(' ')[1])


def run():
    with open('day_two.txt', 'r') as file:
        content = file.read()
        print(day_two(content))


if __name__ == "__main__":
    run()
