from aoc2023.day_one import day_one


def test_day_one():
    coordinates = """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
    """

    assert day_one(coordinates) == 142
