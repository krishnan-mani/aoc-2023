from aoc import day1
import pytest


def test_calibration_value():
    line = "1abc2"
    assert 3 == day1.calibration_value(line)


def test_first_and_last_numbers():
    line = "1abc2"
    assert (1, 2) == day1.first_and_last_numbers(line)


@pytest.mark.parametrize('twople,result', [
    ((1, 2), 3),
])
def test_combine(twople, result):
    assert result == day1.combine(twople)
