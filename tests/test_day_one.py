from aoc2023.day_one import day_one


def test_day_one_pt1():
    coordinates = """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
    """

    assert day_one(coordinates) == 142


def test_day_one_pt2():
    coordinates = """
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
    """

    assert day_one(coordinates) == 281
