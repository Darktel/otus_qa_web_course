from Figure import Figure


class Triangle(Figure):

    def __init__(self, name: str, side_a: float, side_b: float, side_c: float):
        """
        Инициализация экземпляра класса треугольника.
        :type name: str - наименование фигуры.
        :param side_a: float - Сторона треугольника "A".
        :param side_b: float - Сторона треугольника "B".
        :param side_c: float - Сторона треугольника "C".
        """
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = name
        if self.side_a > self.side_b + self.side_c or \
                self.side_b > self.side_a + self.side_c or \
                self.side_c > self.side_b + self.side_a:
            return None

    @property
    def area(self):
        """
        Вычисление площади треугольника по формуле Гирона.
        :return: float or int
        """
        self.__p = 0.5 * (self.side_a + self.side_b + self.side_c)  # Переменная используется при вычислении площади.
        self.__square = (self.__p * (self.__p - self.side_a) * (self.__p - self.side_b) * (
                self.__p - self.side_c)) ** 0.5
        return self.__square

    @property
    def perimeter(self):
        """
        Вычисление периметра треугольника
        :return: float or int
        """
        return self.side_a + self.side_b + self.side_c


if __name__ == '__main__':
    triangle1 = Triangle(side_a=10, side_b=10, side_c=15)
    print(triangle1.area())
    print(triangle1.perimeter())
