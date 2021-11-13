from src.Square import Square


def test_init_square():
    square = Square('Квадрат', 3)
    assert isinstance(square, Square)


def test_check_name():
    square = Square('Квадрат', 3)
    assert square.name == 'Квадрат'


def test_check_side():
    square = Square('Квадрат', 3)
    assert square.side_a == 3


def test_check_perimeter_square():
    square = Square('Квадрат', 5.7)
    assert square.perimeter == 22.8


#  В этом тесте приходиться использовать округление т.к. высчитываемое значение  142.2000000000002 (особенностей Python)
def test_check_area_square():
    square = Square('Квадрат', 15.8)
    assert round(square.area, 5) == 249.64


def test_add_area_to_square():
    square_one = Square('Квадрат1', 7 / 5)
    square_two = Square('Квадрат2', 15.8)
    assert round(square_one.add_area(square_two), 4) == 251.6
