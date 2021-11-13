import pytest

from src.Figure import Figure
from src.Circle import Circle
from src.Square import Square


#  проверка на исключение
def test_init_figure():
    with pytest.raises(Exception):
        figure = Figure('Фигура')


def test_add_area():
    circle = Circle('Круг', 2)
    square = Square('Квадрат', 5)
    assert round(circle.add_area(square), 4) == 37.5664
    assert round(square.add_area(circle), 4) == 37.5664


def test_add_area_to_not_figure():
    circle = Circle('Круг', 2)
    not_figure = 0
    with pytest.raises(ValueError):
        circle.add_area(not_figure)
