# class Auto:
#     auto_name='Lexus'
#     auto_model='RX 405'
#     auto_year=2019
#
#     def on_auto_start(self):
#         print('The engine is on')
#     def off_auto_stop(self):
#         print('The engine is off')
#
# car=Auto()
# print(car)
# car.on_auto_start()
# print(car.auto_name)
#
# car.off_auto_stop()
#
# class Auto():
#     auto_count=0
#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         Auto.auto_count+=1
#         print('The engine is on')
#
# car=Auto()
# car.on_auto_start('Audi', 'x8','2020')
# print(car.auto_count)
#
# car.on_auto_start('Audi', 'x7','2018')
# print(car.auto_count)

# class Auto:
#     # атрибуты класса
#     auto_count = 0
#     # методы класса
#     def __init__(self, auto_name, auto_model):
#         Auto.auto_count += 1
#         self.auto_name=auto_name
#         self.auto_model=auto_model
#         print(Auto.auto_count)
#         print(self.auto_name, self.auto_model)
#
# car=Auto("BMW", "X5")
# car2=Auto("Subaru", "Kashkai")
#
# print(car.auto_name)

class LittleBell():
    def sound(self):
        print('ding')


bell = LittleBell()
bell.sound()


class Button():
    press_count = 0

    def click(self):
        Button.press_count += 1

    def click_count(self):
        return self.press_count

    def reset(self):
        self.press_count = 0


b = Button()
b.click()
b.click()
print(b.press_count)
b.click()
print(b.press_count)


class Balance():
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, right_weigth):
        self.right += right_weigth

    def add_left(self, left_weigth):
        self.left += left_weigth

    def result(self):
        if self.right > self.left:
            print('R')
        elif self.right < self.left:
            print('L')
        else:
            print("=")


balance = Balance()
balance.add_right(10)
balance.add_left(5)
balance.add_left(5)
balance.result()
balance.add_left(5)
balance.result()


class BigBell():
    ding_or_dong = ["ding", "dong"]
    counter = 0

    def sound(self):
        print(self.ding_or_dong[self.counter])
        self.counter = (self.counter + 1) % 2


bell = BigBell()
bell.sound()
bell2 = BigBell()
bell2.sound()


class OddEvenSeparator():
    def __init__(self):
        self.number_list = []

    def add_number(self, number):
        self.number_list.append(number)

    def even(self):
        # return [x for x in self.number_list if x%2==0]
        return list(filter(lambda x: not x % 2, self.number_list))

    def odd(self):
        return [x for x in self.number_list if x % 2 == 1]  # (self.odd_list)


separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(2)
separator.add_number(1)
separator.add_number(0)

print(separator.even())
print(separator.odd())


class MinMaxWordFinder():
    def __init__(self):
        self.text = ''

    def add_sentence(self, sentence):
        if not self.text == "":
            self.text += " "
        self.text += sentence

    def shortest_words(self):
        new_text = self.text.split(' ')
        shortest = [x for x in new_text if len(x) == min(map(len, new_text))]
        shortest.sort()
        return shortest
    #     try:
    #         min_length = len(new_text[0])
    #     except:
    #         return [-1]
    #     for word in new_text:
    #         if len(word) < min_length:
    #             shortest = [word]
    #             min_length = len(word)
    #         elif len(word) == min_length:
    #             shortest.append(word)
    #         else:
    #             continue
    #     shortest.sort()
    #     return shortest
    #
    # def remove_all(self):
    #     self.text = ''

    def longest_words(self):

        new_text = self.text.split(' ')
        longest = [x for x in new_text if len(x) == max(map(len, new_text))]
        longest.sort()
        return list(set(longest))
        # longest = []
        # try:
        #     max_length = len(new_text[0])
        # except:
        #     return [-1]
        # for word in new_text:
        #     if len(word) > max_length:
        #         longest = [word]
        #         max_length = len(word)
        #     elif len(word) == max_length:
        #         longest.append(word)
        #     else:
        #         continue
        # longest.sort()
        # return list(set(longest))

    def remove_all(self):
        self.text = ''


finder = MinMaxWordFinder()
finder.add_sentence('Hello b23 workd')
finder.add_sentence('abc asdf Qwerty')
finder.add_sentence('abc asdffh Qwerty')
print(finder.text)
print(finder.shortest_words())
print(finder.longest_words())
