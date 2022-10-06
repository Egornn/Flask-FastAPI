import sys
import time as time

#time.perf_counter()

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
            if not time.time() - start_time <= self.duration[self.__color]:
                self.__color = color_change(self.__color, self.duration)
                start_time = time.time()
            print(f'From the begining {time.time() - self.initiation_time}s passed. The color is {self.__color}')
            time.sleep(1)


def start_TL():
    traffic_light = TrafficLight()
    traffic_light.running()


start_TL()

class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__mass_per_sm = 25

    def mas_for_road(self, road_thickness):
        return str(self._length * self._width * self.__mass_per_sm * road_thickness / 1000) + " тонн"


def hit_the_road():
    road = Road(5000, 20)
    print(road.mas_for_road(5))


hit_the_road()

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

    def info(self):
        print("Create a worker")


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def info(self):
        print("Creation of a postion")


def do_worker():
    ivan = Position('Ivan', 'Ivanov', "Anume Lover", '10000', '1500')
    print(ivan.get_full_name())
    print(ivan.get_total_income())

do_worker()


class TicTacToeBoard():

    def __init__(self):
        self.__empty_board = [["." for x in range(3)] for y in range(3)]
        self.__current_board = self.__empty_board
        self.__current_player = "X"
        self.__another_player = "O"

    def show_board(self):
        for line in self.__current_board:
            print(line)
        print()


    def new_game(self):
        self.__current_board = self.__empty_board

    def get_field(self):
        return self.__current_board

    def check_field(self):
        t = self.__current_board
        lines = [
            [t[0]],
            [t[1]],
            [t[2]],
            [t[0][0], t[1][0], t[2][0]],
            [t[0][1], t[1][1], t[2][1]],
            [t[0][2], t[1][2], t[2][2]],
            [t[0][0], t[1][1], t[2][2]],
            [t[0][2], t[1][1], t[2][0]],
        ]
        if ["X" for x in range(3)] in lines:
            return "X"
        elif ["O" for x in range(3)] in lines:
            return "O"
        elif not ("_" in t[0] or "_" in t[1] or "_" in t[2]):
            return "D"
        else:
            return None

    def make_move(self, row, col):
        row, col = row - 1, col - 1
        if not self.check_field() == None:
            print("The game is already over")
        else:
            if self.__current_board[row][col] == "_":
                self.__current_board[row][col] = self.__current_player
                self.show_board()
                position = self.check_field()
                if position == "X":
                    print("Congrats to X player")
                elif position == "O":
                    print("Congrats to O player")
                elif position == "D":
                    print("Draw")
                else:
                    print('Next turn')
                    self.__current_player, self.__another_player = \
                        self.__another_player, self.__current_player
            else:
                print(f"This place ({row + 1}, {col + 1}) is already taken")


def play_ttt():
    board = TicTacToeBoard()
    board.show_board()

    board.make_move(2, 2)
    board.make_move(2, 3)
    board.make_move(2, 3)
    board.make_move(3, 1)
    board.make_move(1, 3)
    board.make_move(3, 3)
    board.make_move(3, 3)
    board.make_move(3, 2)
    board.make_move(3, 2)
    board.make_move(2, 1)
    board.make_move(1, 1)
    board.make_move(1, 2)
    board.make_move(1, 2)


play_ttt()


class SeaMap():
    def __init__(self):
        self.empty_map = [["." for x in range(10)] for y in range(10)]
        self.current_map = self.empty_map

    def reset_board(self):
        self.current_map = self.empty_map

    def cell(self, row, col):
        row, col = row - 1, col - 1
        return row + col

    def show_map(self):
        for i in self.current_map:
            print(i)
        print()

    def shot(self, row, col, result):
        row, col = row - 1, col - 1
        if result == "miss":
            self.current_map[row][col] = "*"
        elif result == "hit":
            self.current_map[row][col] = "X"
        elif result == "sink":
            self.current_map[row][col] = "X"
            self.__after_sink(row, col)
            self.__clean_the_S()

    def __clean_the_S(self):
        for row_n in range(len(self.current_map)):
            for col_n in range(len(self.current_map[0])):
                if self.current_map[row_n][col_n] == "S":
                    self.current_map[row_n][col_n] = "X"

    def __bool_adj(self, row, col, target_row, target_col):
        if abs(row - target_row) == 1 and abs(col - target_col) == 0:
            return True
        if abs(row - target_row) == 0 and abs(col - target_col) == 1:
            return True
        return False

    def __diag_adj(self, row, col, target_row, target_col):
        cond = abs(row - target_row) <= 1 and \
               abs(col - target_col) <= 1 and \
               not (row == target_row and col == target_col)
        return cond

    def __after_sink(self, row, col):
        self.current_map[row][col] = "S"
        for row_n in range(len(self.current_map)):
            for col_n in range(len(self.current_map[0])):
                if self.current_map[row_n][col_n] == "X":
                    if self.__bool_adj(row_n, col_n, row, col):
                        self.__after_sink(row_n, col_n)
                elif self.current_map[row_n][col_n] == ".":
                    if self.__diag_adj(row_n, col_n, row, col):
                        self.current_map[row_n][col_n] = "*"


def play_battleship():

    sm = SeaMap()
    sm.shot(8, 2, 'miss')
    sm.show_map()

    sm.shot(8, 3, 'hit')
    sm.show_map()
    sm.shot(8, 4, 'hit')
    sm.show_map()
    sm.shot(6, 5, 'sink')
    sm.show_map()
    sm.shot(8, 5, 'sink')
    sm.show_map()

play_battleship()

def tests():
    test1 = SeaMap()
    test1.shot(3,1, 'miss')
    test1.shot(7,10,"miss")
    test1.show_map()

    test2=SeaMap()
    test2.shot(3,1, 'sink')
    test2.shot(7,10, 'hit')
    test2.show_map()

    test3=SeaMap()
    test3.shot(1,1,"sink")
    test3.shot(1,10,"sink")
    test3.shot(10,1, "sink")
    test3.shot(10,10,"sink")
    test3.show_map()

tests()

