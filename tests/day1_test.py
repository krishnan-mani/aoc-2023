from aoc import day1
import pytest


@pytest.mark.parametrize('line,expected', [
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77)
])
def test_calibration_value(line, expected):
    assert expected == day1.calibration_value(line)


def test_first_and_last_numbers():
    line = "1abc2"
    assert (1, 2) == day1.first_and_last_numbers(line)


@pytest.mark.parametrize('twople,expected', [
    ((1, 2), 12),
])
def test_combine(twople, expected):
    assert expected == day1.combine(twople)
