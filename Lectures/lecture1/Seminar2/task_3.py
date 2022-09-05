# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

search = input('String to search ')
long = input('String to search in ')
if len(search) > len(long):
    search, long = long, search
counter = 0
print(long.count(search))

#Self writed method
str1 = input()
str2 = input()
count = 0
if len(str1) < len(str2):
    len_str1 = len(str1)
    i = 0
    while i < len(str2):
        if str1[0] == str2[i]:
            if str1[1:] == str2[i + 1: i + len_str1]:
                count += 1
                i += len_str1
            else:
                i += 1
        else:
            i += 1
print(count)
