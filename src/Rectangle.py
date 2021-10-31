from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, name: str, side_a: float, side_b: float):
        """
        Инициализация экземпляра класса прямоугольника.
        :param side_a: float - Сторона прямоугольника "A".
        :param side_b: float - Сторона прямоугольника "B".
        """
        self.side_a = side_a
        self.side_b = side_b
        self.name = name

    @property
    def area(self):
        """
        Вычисление площади прямоугольника.
        :return: float or int
        """

        return self.side_a * self.side_b  # Вычисление площади прямоугольника.

    @property
    def perimeter(self):
        """
        Вычисление периметра прямоугольника
        :return: float or int
        """

        return 2 * (self.side_a + self.side_b)
