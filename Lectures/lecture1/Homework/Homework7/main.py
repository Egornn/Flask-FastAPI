# Разделим сервис на этапы:
# Как можно вводить данные?
# ‘Фамилия Имя Номер’
# Как их обрабатывать? Где хранить?
# user = {‘Name’:’’, ‘Last Name’:’’, ‘number’:’’ }
# user_list = [user1,user2,user3……]
# Как запрашивать и получать данные?
# Какие функции можно для этого создать?
# Как вынести функции в модули?
import os

from controller import *

add_data('input.txt', 'data.txt')
cleaner_print(pull_line('Name', 'Иван'))
