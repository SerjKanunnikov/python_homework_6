import re


def import_cookbook():
    dish_list = []
    dish_stats = ["ingredient_name", "quantity", "measure"]
    cook_book = {}
    with open(file="recipes.txt") as f:
        for line in f:
            if re.match('^[а-яА-Я]\D*$', line):
                dish_list.append(line.split(' ', 1)[0].strip())  # создание списка блюд
            if re.match('^\d$', line):
                ingredients_count = int(line)
                print(ingredients_count)
                for line in f:
                    if re.match('^[а-яА-Я]*\s\|\s\d*\s\|\s[а-яА-Я]*$', line):
                        dish_ingredients_list = line.split(" | ")
                        dish_ingredients = dict(zip(dish_stats, dish_ingredients_list))  # создание словарей ингредиентов
                        print(dish_ingredients)

import_cookbook()
