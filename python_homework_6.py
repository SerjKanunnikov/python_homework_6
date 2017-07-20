# -*- coding: utf-8 -*-

import re


def import_cookbook():
    dish_list = []
    dishes_with_ingredients = []
    dish_number = 0
    dish_stats = ["ingredient_name", "quantity", "measure"]
    cook_book = {}
    with open(file="recipes.txt") as f:
        for line in f:
            if re.match('^[а-яА-Я]\D*$', line):
                dish_list.append(line.split(' ', 1)[0].strip())  # создание списка блюд
                # print(dish_list)
            if re.match('^\d$', line):
                ingredients_count = int(line)
                dish_number += 1  # номер блюда из списка
                # print(ingredients_count)
            if re.match('^[а-яА-Я]*\s\|\s\d*\s\|\s[а-яА-Я]*$', line):
                dish_ingredients_list = line.split(" | ")
                dish_ingredients = dict(zip(dish_stats, dish_ingredients_list))  # создание словарей ингредиентов
                dishes_with_ingredients.append(dish_ingredients)  # список словарей ингредиентов
                cook_book.update({dish_list[dish_number-1]: dishes_with_ingredients[0:ingredients_count]})
    print(cook_book)

import_cookbook()
