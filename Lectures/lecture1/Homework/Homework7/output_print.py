from keys import keys

def cleaner_print(output):
    global keys
    for dict in output:
        result = ''
        for i in range(len(dict)):
            result += f'{keys[i]} : {dict[keys[i]]}; '
        if output[-1] == dict:
            print(result[:-2])
        else:
            print(result[:-1])
