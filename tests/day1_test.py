from aoc import day1
import pytest


@pytest.mark.parametrize('line,expected', [
    ("two1nine", 29),
])
def test_corrected_calibration_value(line, expected):
    assert expected == day1.corrected_calibration_value(line)


def test_replace_all_literals():
    line = "zeroonetwothreefourfivesixseveneightnine"
    assert "0123456789" == day1.replace_all_literals(line)


def test_literals_to_digit():
    assert "a1b" == day1.literals_to_digit("aoneb", "one", 1)


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
