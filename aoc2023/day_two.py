#!/usr/bin/env python3
from functools import reduce

default_bag = dict(red=12, green=13, blue=14)


def day_two_pt1(raw_games: str) -> int:
    games = parse_games(raw_games)

    possible_games = list(filter(lambda game: game_possible(game, default_bag), games))

    return sum_game_ids(possible_games)


def parse_games(games: str) -> list[dict[str, int]]:
    lines: list[str] = games.split('\n')

    result = []
    for line in lines:
        game, sets = line.split(': ')

        result.append(dict(id=parse_game_id(game), sets=parse_sets(sets)))

    return result


def parse_game_id(game: str) -> int:
    return int(game.split(' ')[1])


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


def set_possible(a_set: dict[str, int], bag: dict[str, int]) -> bool:
    for color, count in a_set.items():
        if color not in bag or count > bag[color]:
            return False
    return True


def game_possible(game, bag: dict) -> bool:
    for a_set in game['sets']:
        if not set_possible(a_set, bag):
            return False
    return True


def sum_game_ids(games) -> int:
    return sum(map(lambda game: game['id'], games))


def day_two_pt2(raw_games: str) -> int:
    games = parse_games(raw_games)

    min_cubes_for_games = list(map(min_cubes_for_game, games))
    power_of_min_cubes = list(map(power_of_set, min_cubes_for_games))

    return sum(power_of_min_cubes)


def power_of_set(a_set: dict[str, int]) -> int:
    # multiply all values in a_set
    counts_per_color = a_set.values()
    return reduce(lambda x, y: x * y, counts_per_color)


def min_cubes_for_game(game) -> dict[str, int]:
    min_cubes = dict(red=0, green=0, blue=0)
    for a_set in game['sets']:
        for color, count in a_set.items():
            if count > min_cubes[color]:
                min_cubes[color] = count
    return min_cubes


def run():
    with open('day_two.txt', 'r') as file:
        content = file.read()
        print(f'pt1: {day_two_pt1(content)}')
        print(f'pt2: {day_two_pt2(content)}')


if __name__ == "__main__":
    run()
