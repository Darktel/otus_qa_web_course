from src.Figure import Figure


class Circle(Figure):

    def __init__(self, name: str, radius: float):
        """
        Инициализация экземпляра класса круга.
        :param radius: float - Радиус круга.
        """
        from math import pi
        self.__pi = pi
        self.radius = radius
        self.name = name

    @property
    def area(self):
        """
        Вычисление площади круга.
        :return: float or int
        """
        return self.__pi * self.radius ** 2  # Вычисление площади круга.

    @property
    def perimeter(self):
        """
        Вычисление периметра круга
        :return: float or int
        """
        self.__perimeter = 2 * self.__pi * self.radius
        return self.__perimeter
