import math


# General
def make(cls, *args):
    return cls["_new"](*args)


def call(shape, method_name, *args, **kwargs):
    method = find(shape["_class"], method_name)
    return method(shape, *args, **kwargs)


def find(cls, method_name):
    while cls is not None:
        if method_name in cls:
            return cls[method_name]
        cls = cls["_parent"]
    raise NotImplementedError(f"Method '{method_name}' not found in class hierarchy.")


def find_recursive(cls, method_name):
    if method_name in cls:
        return cls[method_name]
    parent_cls = cls["_parent"]
    if parent_cls is not None:
        return find_recursive(parent_cls, method_name)
    raise NotImplementedError(f"Method '{method_name}' not found in class hierarchy.")


def instanceof(obj, class_type):
    return obj["_class"] == class_type


# Shape, parent
def shape_density(shape, weight):
    return weight / call(shape, "area")


def shape_new(name):
    return {
        "name": name,
        "_class": Shape
    }


Shape = {
    "density": shape_density,
    "_parent": None,
    "_new": shape_new
    # _class-name: "Shape"
}


# Rectangle, child
def rectangle_new(name, width, height):
    return make(Shape, name) | {
        "width": width,
        "height": height,
        "_class": Rectangle
    }


def rectangle_perimeter(shape):
    return shape["width"] + 2 * shape["height"]


def rectangle_area(shape):
    return shape["width"] * shape["height"]


def rectangle_larger(shape, size):
    return call(shape, "area") > size


Rectangle = {
    "perimeter": rectangle_perimeter,
    "area": rectangle_area,
    "larger": rectangle_larger,
    "_parent": Shape,
    "_new": rectangle_new
    # "_class-name": "Rectangle"
}


# Square, child
def square_new(name, side):
    return make(Shape, name) | {
        "side": side,
        "_class": Square
    }


def square_perimeter(shape):
    return shape["side"] * 4


def square_area(shape):
    return shape["side"] ** 2


def square_larger(shape, size):
    return call(shape, "area") > size


Square = {
    "perimeter": square_perimeter,
    "area": square_area,
    "larger": square_larger,
    "_parent": Rectangle,
    "_new": square_new
    # "_class-name": "Square"
}


# Circle, child
def circle_perimeter(shape):
    return shape["side"] * math.pi * 2


def circle_area(shape):
    return math.pi * shape["side"] ** 2


def circle_larger(shape, size):
    return call(shape, "area") > size


def circle_new(name, side):
    return make(Shape, name) | {
        "side": side,
        "_class": Circle
    }


Circle = {
    "perimeter": circle_perimeter,
    "area": circle_area,
    "larger": circle_larger,
    "_parent": Shape,
    "_new": circle_new
    # "_class-name": "Circle"
}


examples = [make(Square, "rc", 4), make(Circle, "ci", 2)]
for ex in examples:
    n = ex["name"]
    d = call(ex, "density", weight=2)
    print(f"{n}: {d:.2f}")
    print(instanceof(ex, Square))