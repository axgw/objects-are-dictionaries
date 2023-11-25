import math


def square_perimeter(shape):
    return shape["side"] * 4


def square_area(shape):
    return shape["side"] ** 2


def square_new(name, side):
    return {
        "name": name,
        "side": side,
        "perimeter": square_perimeter,
        "area": square_area
    }


def circle_perimeter(shape):
    return shape["side"] * math.pi * 2


def circle_area(shape):
    return math.pi * shape["side"] ** 2


def circle_new(name, side):
    return {
        "name": name,
        "side": side,
        "perimeter": circle_perimeter,
        "area": circle_area
    }
