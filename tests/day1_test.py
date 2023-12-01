from aoc import day1
import pytest


@pytest.mark.parametrize('line,expected', [
    ("1abc2", 3)
])
def test_calibration_value(line, expected):
    assert expected == day1.calibration_value(line)


def test_first_and_last_numbers():
    line = "1abc2"
    assert (1, 2) == day1.first_and_last_numbers(line)


@pytest.mark.parametrize('twople,expected', [
    ((1, 2), 3),
])
def test_combine(twople, expected):
    assert expected == day1.combine(twople)
