if __name__ == "__main__":
    class Housing:
        """Жильё"""
        def __init__(self, living_area: float, air_temperature: int, number_of_rooms: int):
            self.living_area = living_area
            self.air_temperature = air_temperature
            self._number_of_rooms = 3
            self.set_number_of_rooms(number_of_rooms)

        def set_number_of_rooms(self, new_number_of_rooms) -> None:
            """Устанавливает количество комнат,
            я хочу минимум трёхкомнатную квартиру, поэтому решил сделать
            соответствующий атрибут защищённым"""
            if not isinstance(new_number_of_rooms, int):
                raise TypeError
            if new_number_of_rooms <= 0:
                raise ValueError
            self._number_of_rooms = new_number_of_rooms

        def set_air_temperature(self, new_air_temperature: int) -> None:
            """Устанавливает новую температуру воздуха в помещении"""
            if not isinstance(new_air_temperature, int):
                raise TypeError
            if not 15 < new_air_temperature < 35:
                raise ValueError
            self.air_temperature = new_air_temperature

        def get_area(self) -> float:
            """Возвращает площадь жилья"""
            return self.living_area

        def __str__(self) -> str:
            return f'Температура воздуха в помещении {self.air_temperature} °C'

        def __repr__(self) -> str:
            return f'Жилая площадь {self.living_area!r} м^2'

    class Flat(Housing):
        """Квартира"""
        def __init__(self, living_area: float, air_temperature: int, number_of_rooms: int, floor_number: int):
            super().__init__(living_area, air_temperature, number_of_rooms)
            self.floor_number = floor_number

        def __repr__(self) -> str:
            return f'Жилая площадь {self.living_area!r} м^2, этаж {self.floor_number!r}'

    class House(Housing):
        """Дом"""
        def __init__(self, living_area: float, air_temperature: int, number_of_rooms: int, garden_area: float):
            super().__init__(living_area, air_temperature, number_of_rooms)
            self.garden_area = garden_area

        def __repr__(self) -> str:
            return f'Жилая площадь {self.living_area!r} м^2, площадь участка {self.garden_area!r}'

        def get_area(self) -> float:
            """Возвращает площадь жилья, которая состоит
            из площади дома и площади участка"""
            return self.living_area + self.garden_area
