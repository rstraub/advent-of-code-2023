from aoc2023.day_one import day_one


def test_day_one():
    input = """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
    """

    assert day_one(sanitize_input(input)) == 1


def sanitize_input(input: str) -> str:
    return input.replace(" ", "")[1:-1]
