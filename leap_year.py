"""
To run this file run it with python 3(python(3) james_taylor_hw1.py) and you will be prompted to enter a year.
Once prompted enter a positive integer and the program will tell you if that year is a leap year.
"""

from typing import Callable

def validate_int(a: str) -> bool:
    try:
        int(a)
    except ValueError:
        print("Year entered was not an integer.")
        return False
    return True


def int_input(msg: str, validate: Callable[[str], bool]=validate_int) -> int:
    answer = input(msg)
    while not validate(answer):
        answer = input(msg)
    return int(answer)


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def validate_year(a: int) -> bool:
    if a > 0:
        return True
    print("Years cannot be negative.")
    return False

def validated_is_leap_year(s: str):
    if not validate_int(s):
        raise TypeError("String is not an int.")
    if not validate_year(int(s)):
        raise ValueError("String is not a positive integer.")
    year = int(s)
    return is_leap_year(year)

if __name__ == "__main__":
    year = int_input("Please enter a year: ", lambda x: validate_int(x) and validate_year(int(x)))
    print(f"The year {year} {'is' if is_leap_year(year) else 'is not'} a leap year.")
