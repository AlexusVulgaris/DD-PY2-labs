import doctest
from typing import Union


class Music:
    def __init__(self, volume: Union[int, float], composition: str):# TODO Написать 3 класса с документацией и аннотацией типов
        """
        Создание и подготовка к работе объекта

        :param volume: Громкость музыки
        :param composition: Музыкальное произведение

        Пример:
        >>> music = Music(80, "Классика")  # инициализация экземпляра класса
        """
        self.volume = volume
        self.composition = composition

        if not isinstance(volume, int):
            raise TypeError("Громкость музыки задаётся только целыми числами!")
        if 0 < volume < 100:
            raise ValueError("Громкость музыки регулируется в пределах от 0 до 100")

        if composition == 'Рэп':
            raise TypeError("Можно указывать только жанры музыки!")

    def changing_the_volume(self, new_volume: int) -> int:
        """
        Функция меняет громкость музыки

        :param new_volume: Новая громкость музыки
        :return: Изменённая громкость музыки

        Пример:
        >>> music = Music(80, "Классика")
        >>> music.changing_the_volume(50)
        """
        if not isinstance(new_volume, int):
            raise TypeError("Громкость музыки задаётся только целыми числами!")
        if 0 < new_volume < 100:
            raise ValueError("Громкость музыки регулируется в пределах от 0 до 100")
        ...

    def changing_the_composition(self, new_composition: str) -> str:
        """
        Функция меняет музыкальное произведение

        :param new_composition: Новое музыкальное произведение
        :return: Новое музыкальное произведение

        Пример:
        >>> music = Music(80, "Классика")
        >>> music.changing_the_composition('Рок')
        """
        if not isinstance(new_composition, str):
            raise TypeError("Музыка указывается типом данных Строка")
        ...


class Lamp:
    def __init__(self, brightness: Union[int, float], activation: bool):
        """
        Создание и подготовка к работе объекта

        :param brightness: Яркость
        :param activation: Включение или выключение

        Пример:
        >>> lamp = Lamp(100, True)
        """
        self.brightness = brightness
        self.activation = activation

        if not isinstance(brightness, int):
            raise TypeError("Яркость регулируется только целыми числами")
        if 0 < brightness < 100:
            raise ValueError("Яркость регулируется по шкале от 0 до 100")

        if not isinstance(activation, bool):
            raise TypeError

    def changing_the_brightness(self, new_brightness: int) -> int:
        """
        Функция меняет мощность освещения

        :param new_brightness: Новая освещённость
        :return: Новая освещённость

        Пример:
        >>> lamp = Lamp(100, True)
        >>> lamp.changing_the_brightness(10)
        """
        ...

    def shutdown(self, new_activation: bool) -> None:
        """
        Функция выключает свет

        :param new_activation: Выключение света
        :return: Выключает свет

        Пример:
        >>> lamp = Lamp(100, True)
        >>> lamp.shutdown(False)
        """
        ...


class Table:
    def __init__(self, length: Union[int, float], width: Union[int, float], height: Union[int, float]):
        """
        Создание и подготовка к работе объекта

        :param length: Длина
        :param width: Ширина
        :param height: Высота

        Пример:
        >>> table = Table(1.5, 1, 0.8)
        """
        self.length = length
        self.width = width
        self.height = height

        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Размеры стола задаются только целыми или дробными числами")

    def changing_the_length(self, new_length: Union[int, float]) -> Union[int, float]:
        """
        Функция устанавливает новую длину стола

        :param new_length: Новая длина стола
        :return: Новая длина стола

        Пример:
        >>> table = Table(1.5, 1, 0.8)
        >>> table.changing_the_length(1.2)
        """
        ...

    def changing_the_width(self, new_width: Union[int, float]) -> Union[int, float]:
        """
        Функция устанавливает новую ширину стола

        :param new_width: Новая ширина стлола
        :return: Новая ширина стола

        Пример:
        >>> table = Table(1.5, 1, 0.8)
        >>> table.changing_the_width(0.5)
        """
        ...

    def changing_the_height(self, new_height: Union[int, float]) -> Union[int, float]:
        """
        Функция устанавливает новую высоту стола

        :param new_height: Новая высота стлола
        :return: Новая высота стола

        Пример:
        >>> table = Table(1.5, 1, 0.8)
        >>> table.changing_the_height(0.7)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации# TODO работоспособность экземпляров класса проверить с помощью doctest
