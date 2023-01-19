from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')


def calculateSquareRoot(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float):
    """Проверяет число, если больше 0 - вычисляем."""
    if your_number <= 0:
        return
    print("Мы вычислили квадратный корень из введённого вами числа."
          f" Это будет: {calculateSquareRoot(your_number)}")


print(message)
calc(25.5)
