import re


def import_cookbook():
    cook_book = {}
    ingredient_stats = ["ingredient_name", "quantity", "measure"]  # свойства ингредиента
    with open(file="recipes.txt", encoding="utf-8") as f:
        for line in f:
            if not re.match('^\d$', line):
                if re.match('^\w*\W*\D*\d*$', line):  # регулярка для поиска названий блюд
                    current_dish = line.strip()
                    ingredients_list = []
                    continue
                if re.match('^(\w*\s)*\|\s\d*\s\|\s\w*$', line):  # регулярка для поиска строки со свойствами ингредиента
                    dish_ingredients_list = line.strip().split(" | ")
                    ingredients_list.append(dict(zip(ingredient_stats, dish_ingredients_list)))  # список словарей ингредиентов
                if not line.strip():
                    ingredients_list = []
                cook_book.update({current_dish: ingredients_list})
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] = int(new_shop_list_item['quantity']) * person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list(cook_book):
    person_count = int(input('Введите количество человек: '))
    dishes = [x.strip() for x in input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')]
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)


create_shop_list(import_cookbook())
