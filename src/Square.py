from src.Figure import Figure


class Square(Figure):

    def __init__(self, name: str, side_a: float):
        """
        Инициализация экземпляра класса квадрата.
        :param side_a: float - Сторона квадрата "A".
        """
        self.side_a = side_a
        self.name = name

    @property
    def area(self):
        """
        Вычисление площади квадрата.
        :return: float or int
        """
        return self.side_a ** 2  # Вычисление площади прямоугольника.

    @property
    def perimeter(self):
        """
        Вычисление периметра квадрата
        :return: float or int
        """
        return 4 * self.side_a


if __name__ == '__main__':
    triangle1 = Square('', side_a=7)
    print(triangle1.area())
    print(triangle1.perimeter())
