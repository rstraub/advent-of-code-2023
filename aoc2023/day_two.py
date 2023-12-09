#!/usr/bin/env python3
from typing import List, Dict, Any


def day_two(games: str) -> int:
    return 1


def parse_games(games: str) -> list[dict[str, int]]:
    lines: list[str] = games.split('\n')

    result = []
    for line in lines:
        game, sets = line.split(':')
        game_id = int(game.split(' ')[1])
        result.append({
            'id': game_id
        })

    return result


def run():
    with open('day_two.txt', 'r') as file:
        content = file.read()
        print(day_two(content))


if __name__ == "__main__":
    run()
