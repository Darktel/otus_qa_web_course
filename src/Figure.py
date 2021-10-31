class Figure:

    def __init__(self, name=None):
        if self.__class__ == Figure:
            raise Exception('Нельзя создавать экземпляры класса Figure')
        self.name = name

    @property
    def perimeter(self) -> int:
        pass

    @property
    def area(self) -> int:
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('При вычислении добавленной площади, передан не верный класс')
        return self.area + figure.area


if '__main__' == __name__:
    figure = Figure('Фигура')