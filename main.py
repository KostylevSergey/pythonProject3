import os
# from pprint import pprint
#
# file_name = 'Recipe_book.txt'
#
# def recipe_catalog(recipe_book):
#     with open(recipe_book, 'r', encoding='utf-8') as recipes:
#         result = {}
#         for line in recipes:
#             dish_name = line.strip()
#             goods = []
#             for item in range(int(recipes.readline())):
#                 ingridients = {}
#                 contents = recipes.readline().split(' | ')
#                 ingridients['ingridient_name'] = contents[0]
#                 ingridients['quantity'] = contents[1]
#                 ingridients['measure'] = contents[2].strip()
#                 goods.append(ingridients)
#             result[dish_name] = goods
#             recipes.readline()
#         return result
#
#
# def get_shop_list_by_dishes(dishes, person_count):
#     result = {}
#     cook_book = recipe_catalog(file_name)
#     for dish in list(cook_book.keys()):
#         if dish not in dishes:
#             cook_book.pop(dish)
#
#     for dish, ingridients in cook_book.items():
#
#         for ingridient in ingridients:
#             if list(ingridient.values())[0] not in result.keys():
#                 lib = {}
#                 lib[list(ingridient.keys())[2]] = list(ingridient.values())[2]
#                 lib[list(ingridient.keys())[1]] = int(list(ingridient.values())[1]) * person_count
#                 result[list(ingridient.values())[0]] = lib
#             elif list(ingridient.values())[0] in result.keys():
#                 my_dict = result[list(ingridient.values())[0]]
#                 sum = (int(list(my_dict.values())[1] / person_count) + int(list(ingridient.values())[1])) * person_count
#                 lib = {}
#                 lib[list(ingridient.keys())[2]] = list(ingridient.values())[2]
#                 lib[list(ingridient.keys())[1]] = sum
#                 result[list(ingridient.values())[0]] = lib
#
#     return result
#
# pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Салат Морковный'], 2))

file_1 = '1.txt'

file_2 = '2.txt'

file_end = 'final.txt'

files = [file_1, file_2]

def file_compiler(file_dict, filef):
    comparison_list = []

    for file in file_dict:
        with open(file, 'r', encoding='utf-8') as file_obj:
            count = 0
            for line in file_obj:
                count += 1

        with open(file, 'r', encoding='utf-8') as file_obj:
            text = file_obj.readlines()
        comparison_list.append((count, file, text))
    fin = sorted(comparison_list)


    with open(filef, 'w', encoding='utf-8') as file_obj:
        for file in fin:
            file_obj.write(f'\n{file[1]}\n')
            file_obj.write(f'{file[0]}\n')
            for line in file[2]:
                file_obj.write(line)



file_compiler(files, file_end)









