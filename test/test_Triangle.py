from src.Triangle import Triangle


def test_init_triangle():
    triangle = Triangle('Треугольник', 3,4,5)
    assert isinstance(triangle, Triangle)

def test_init_wrong_triangle():
    triangle = Triangle('Треугольник', 7,111,5)
    assert isinstance(triangle, Triangle)
    assert triangle.side_a is None

def test_check_name():
    triangle = Triangle('Треугольник', 3,4,5)
    assert triangle.name == 'Треугольник'


def test_check_side():
    triangle = Triangle('Треугольник', 3,4,5)
    assert triangle.side_a == 3
    assert triangle.side_b == 4
    assert triangle.side_c == 5

def test_check_side():
    triangle = Triangle('Треугольник', 3,4,5)
    assert triangle.side_a == 3
    assert triangle.side_b == 4
    assert triangle.side_c == 5

def test_check_perimeter_triangle():
    triangle = Triangle('Треугольник', 5.7,4,2)
    assert triangle.perimeter == 11.7


#  В этом тесте приходиться использовать округление т.к. высчитываемое значение  142.2000000000002 (особенностей Python)
def test_check_area_triangle():
    triangle = Triangle('Треугольник', 15.8)
    assert round(triangle.area, 5) == 249.64


def test_add_area_to_triangle():
    triangle_one = Triangle('Треугольник1', 7 / 5)
    triangle_two = Triangle('Треугольник2', 15.8)
    assert round(triangle_one.add_area(triangle_two), 4) == 251.6
