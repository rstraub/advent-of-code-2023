from aoc2023.day_two import day_two, parse_games, parse_set, parse_sets, set_possible, game_possible, sum_game_ids
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


def test_set_possible_returns_true_given_cubes_dont_exceed_bag_capacity():
    bag = {
        'blue': 1,
    }

    a_set = bag

    assert set_possible(a_set, bag)


def test_set_possible_returns_false_given_cubes_exceed_bag_capacity():
    bag = {
        'red': 1,
    }

    a_set = {
        'red': 2,
    }

    assert not set_possible(a_set, bag)


def test_set_possible_returns_false_given_cube_color_missing_in_bag():
    bag = {
        'blue': 1,
    }

    a_set = {
        'red': 1,
    }

    assert not set_possible(a_set, bag)


def test_game_possible_returns_true_given_all_sets_possible():
    bag = {
        'red': 1,
        'blue': 1,
    }

    game = {
        'id': 1,
        'sets': [{
            'red': 1,
        }, {
            'blue': 1,
        }]
    }

    assert game_possible(game, bag)


def test_game_possible_returns_false_given_any_set_impossible():
    bag = {
        'red': 1,
        'blue': 1,
    }

    game = {
        'id': 1,
        'sets': [{
            'red': 2,
        }, {
            'blue': 1,
        }]
    }

    assert not game_possible(game, bag)


def test_sum_game_ids():
    game1 = dict(id=1)
    game2 = dict(id=4)

    assert sum_game_ids([game1, game2]) == 5
