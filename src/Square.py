from src.Figure import Figure
from src.Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, name: str, side_a: int):
        """
        Инициализация экземпляра класса прямоугольника.
        :param side_a: float - Сторона квадрата "A".
        :param side_b: float - Сторона квадрата "B".
        """
        super().__init__(name, side_a, side_a)
