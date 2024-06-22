from random import randint


def random_six_digits() -> str:
    return str(randint(100000, 999999))
