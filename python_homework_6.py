import json
import re


def import_cookbook():
    cook_book = {}
    dish_list = []  # список блюд
    # ingredients_list = []  # список ингридиентов
    dish_number = 0  # номер блюда для использования в списке
    ingredient_stats = ["ingredient_name", "quantity", "measure"]  # свойства ингридиента
    ingredients_count = 0  # счетчик ингредиентов
    left_index = 0  # левая граница для перебора списка ингредиентов
    ingredients_count_list = []
    with open(file="recipes.txt", encoding="utf-8") as f:
        for line in f:
            if re.match('^[а-яА-Я]\W*\D*\d*$', line):  # регулярка для поиска названий блюд
                dish_list.append(line.split(' ', 1)[0].strip())  # создание списка блюд
                left_index += ingredients_count
                current_dish = line.strip()
                ingredients_list = []
                continue
            if re.match('^\d$', line):  # регулярка для поиска количества ингредиентов
                ingredients_count = int(line)
                dish_number += 1  # номер блюда из списка
                ingredients_count_list.append(ingredients_count)
                continue
            if re.match('^([а-яА-Я]*\s)*\|\s\d*\s\|\s[а-яА-Я]*$', line):  # регулярка для поиска строки со свойствами ингредиента
                dish_ingredients_list = line.strip().split(" | ")
                ingredients_list.append(dict(zip(ingredient_stats, dish_ingredients_list))) # список словарей ингредиентов
                if not line.strip():
                    cook_book.update({current_dish.strip(): ingredients_list})
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
