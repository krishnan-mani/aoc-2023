def calibration_value(line):
    return combine(first_and_last_numbers(line))


def first_and_last_numbers(line):
    numbers = list(filter(lambda x: x.isdigit(), line))
    return (int(numbers[0]), int(numbers[-1]))


def combine(twople):
    return twople[0] + twople[1]
