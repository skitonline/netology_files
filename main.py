def create_cook_book(path):
    result = {}
    with open(path, encoding='utf-8') as file:
        dish = file.readline()
        while dish != '':
            dish = dish.strip()
            result[dish] = []
            try:
                quantity = int(file.readline().strip())
            except ValueError:
                print('Неверный формат данных')
                return None
            for ingredient in range(quantity):
                ingredient_line = file.readline()
                ingredient_list = ingredient_line.split('|')
                if len(ingredient_list) != 3:
                    print('Неверный формат данных')
                    return None
                try:
                    result[dish].append({'ingredient_name': ingredient_list[0].strip(),
                                         'quantity': int(ingredient_list[1].strip()),
                                         'measure': ingredient_list[2].strip()})
                except ValueError:
                    print('Неверный формат данных')
                    return None
            file.readline()
            dish = file.readline()
    return result


cook_book = create_cook_book('list.txt')
for k, v in cook_book.items():
    print(k)
    for dish in v:
        print(dish)
    print()


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish not in cook_book:
            print('Данного блюда нет в кулинарной книги')
            return None
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in result:
                result[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                         'quantity': ingredient['quantity']}
            else:
                result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
    return result


shop_list_by_dishes = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
for k, v in shop_list_by_dishes.items():
    print(k, v)
    print()


def unite_files(*paths):
    result_string = ''
    file_info = []
    for path in paths:
        with open(path, encoding='utf-8') as file:
            lines = file.readlines()
            file_info.append((path, len(lines), lines))
    file_info = sorted(file_info, key=lambda file_info: file_info[1])
    for info in file_info:
        result_string += info[0] + '\n' + str(info[1]) + '\n'
        for line in info[2]:
            result_string += line
        result_string += '\n'
    with open ('result.txt', 'w', encoding='utf-8') as result_file:
        result_file.write(result_string)


unite_files('1.txt', '2.txt', '3.txt')
