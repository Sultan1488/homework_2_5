example = {
    'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15/2, False],
    'fire': ['hot', 46, ['cha', 'ching'], 81.13],
    'earth': ['solid', 100, (13, 31, 1), 90.01, {'b': 'c'}]
    }
elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']


def func(dict_1, list_1):
    for element in list_1:
        try:
            sum_value = 0
            for value_1 in dict_1[element]:
                try:
                    sum_value += value_1
                except TypeError:
                    continue
            print(f'{element}: {sum_value}')
        except KeyError:
            print(f'The {element} key is missing!!!')
func(example, elements)
