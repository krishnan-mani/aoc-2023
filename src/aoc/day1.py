import functools


literals = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
literals_with_digits = [(literals[x], x) for x in range(10)]


def corrected_calibration_value(line):
    return combine(first_and_last_numbers(replace_all_literals(line)))


def replace_all_literals(line):
    return functools.reduce(lambda x,y: literals_to_digit(x, y[0], y[-1]), literals_with_digits, line)


def literals_to_digit(_str, literal, digit):
    return _str.replace(literal, str(digit))


def calibration_value(line):
    return combine(first_and_last_numbers(line))


def first_and_last_numbers(line):
    numbers = list(filter(lambda x: x.isdigit(), line))
    return (int(numbers[0]), int(numbers[-1]))


def combine(twople):
    return (twople[0] * 10) + twople[1]


if __name__ == "__main__":
    f = open('src/resources/day1.txt', 'r')
    sum = functools.reduce(lambda x,y: x + calibration_value(y), f.readlines(), 0)
    print(f"Day 1, problem 1: sum of calibration values: {sum}")
