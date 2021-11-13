from src.Rectangle import Rectangle


def test_init_rectangle():
    rectangle = Rectangle('Прямоугольник', 3, 6)
    assert isinstance(rectangle, Rectangle)


def test_check_name():
    rectangle = Rectangle('Прямоугольник', 3, 7)
    assert rectangle.name == 'Прямоугольник'


def test_check_sides():
    rectangle = Rectangle('Прямоугольник', 3, 2)
    assert rectangle.side_a == 3
    assert rectangle.side_b == 2


def test_check_perimeter_rectangle():
    rectangle = Rectangle('Прямоугольник', 5.7, 26.99)
    assert rectangle.perimeter == 65.38


#  В этом тесте приходиться использовать округление т.к. высчитываемое значение  142.2000000000002 (особенностей Python)
def test_check_area_rectangle():
    rectangle = Rectangle('Прямоугольник', 15.8, 9)
    assert round(rectangle.area, 5) == 142.2


def test_add_area_to_rectangle():
    rectangle_one = Rectangle('Прямоугольник1', 7 / 5, 52.999)
    rectangle_two = Rectangle('Прямоугольник2', 15.8, 2 ** 3)
    assert rectangle_one.add_area(rectangle_two) == 200.5986
