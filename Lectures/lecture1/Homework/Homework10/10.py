import time as time


# Traffic light

class TrafficLight():
    def __init__(self):
        self.__color = 'red'
        self.duration = {"red": 7, "yellow": 2, "green": 3}
        self.initiation_time = time.time()

    def running(self):
        def color_change(current_color, duration):
            temp = iter(duration)
            for key in temp:
                if key == current_color:
                    return next(temp, "red")

        start_time = time.time()
        initial_time = self.initiation_time
        while start_time - initial_time > self.duration[self.__color]:
            initial_time += self.duration[self.__color]
            self.__color = color_change(self.__color, self.duration)
        end_time = start_time + 20

        while time.time() < end_time:
            if time.time() - start_time <= self.duration[self.__color]:
                print(self.__color)
            else:
                self.__color = color_change(self.__color, self.duration)
                print(self.__color)
                start_time = time.time()
            time.sleep(1)


traffic_light = TrafficLight()
traffic_light.running()


class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__mass_per_sm = 25

    def mas_for_road(self, road_thickness):
        return str(self._length * self._width * self.__mass_per_sm * road_thickness / 1000) + " тонн"


road = Road(5000, 20)
print(road.mas_for_road(5))


# 3. Реализовать базовый класс Worker (работник):
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров

class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), "bonus": int(bonus)}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]
ivan=Position('Ivan', 'Ivanov', "Anume Lover", '10000', '1500')
print(ivan.get_full_name())
print(ivan.get_total_income())