from aoc2023.day_two import day_two, parse_games
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
    }, {
        'id': 2,
    }]
