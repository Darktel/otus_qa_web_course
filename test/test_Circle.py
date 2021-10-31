from src.Circle import Circle
from math import pi

def test_init_circle():
    circle = Circle('Круг', 3)
    assert isinstance(circle, Circle)

def test_check_name():
    circle = Circle('Круг', 3)
    assert circle.name == 'Круг'

def test_check_radius():
    circle = Circle('Круг', 3)
    assert circle.radius == 3

def test_check_perimeter_circle():
    circle = Circle('круг', 5)
    assert circle.perimeter == 2 * pi * 5

def test_check_area_circle():
    circle = Circle('круг', 15.8)
    assert circle.area == pi * 15.8 ** 2

def test_add_area_to_circle():
    circle_one = Circle('круг1', 7/5)
    circle_two = Circle('круг2', 15.8)
    assert circle_one.add_area(circle_two) == 790.424711643192