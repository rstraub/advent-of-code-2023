from aoc2023.day_two import day_two, parse_games, parse_set, parse_sets
from aoc2023.utils.input_reader import sanitize


def test_day_two_pt1():
    games = sanitize("""
     Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
     Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
     Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
     Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
     Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """)

    assert day_two(games) == 8


def test_parse_games():
    games = sanitize("""
        Game 1: 3 blue
        Game 2: 1 red 
   """)

    assert parse_games(games) == [{
        'id': 1,
        'sets': [{'blue': 3}]
    }, {
        'id': 2,
        'sets': [{'red': 1}]
    }]


def test_parse_set():
    a_set = "1 red, 2 green, 6 blue"

    assert parse_set(a_set) == {
        'red': 1,
        'green': 2,
        'blue': 6,
    }


def test_parse_multiple_sets():
    sets = "1 red; 2 green, 6 blue"

    assert parse_sets(sets) == [{
        'red': 1
    }, {
        'green': 2,
        'blue': 6,
    }]
