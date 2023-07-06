def get_default(data: dict, key: int | str, value: int | str = 1):
    try:
        result = data[key]
    except KeyError as e:
        result = value
    return result


if __name__ == '__main__':
    print(get_default({1: '1', 2: '2', 3: '3'}, 4))
