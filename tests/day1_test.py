from aoc import day1


def test_calibration_value():
    line = "1abc2"
    assert 3 == day1.calibration_value(line)


def test_first_and_last_numbers():
    line = "1abc2"
    assert (1, 2) == day1.first_and_last_numbers(line)



def test_combine():
    assert 3 == day1.combine((1, 2))
