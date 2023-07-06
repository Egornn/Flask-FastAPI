def num_exc():
    while True:
        num = input('Input positive int or float: ')
        try:
            num = int(num)
            break
        except ValueError as e:
            try:
                num = float(num)
                break
            except ValueError as e:
                print(f'Incorrect value: {e}\n')
    return num


if __name__ == '__main__':
    print(type(num_exc()))
