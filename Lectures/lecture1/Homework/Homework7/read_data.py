from keys import keys

def input_read(path):
    try:
        f = open(path, "r", encoding='UTF8')
    except:
        print('Input does not exist')
        exit()
    temp = f.read().split('\n')
    f.close()
    lines = []
    for elem in temp:
        temp_dict = {}
        person = elem.split(' ')
        for i in range(len(person)):
            temp_dict[keys[i]] = person[i]
        lines.append(temp_dict)
    return lines