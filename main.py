from pprint import pprint

file_name = 'Recipe_book.txt'

def recipe_catalog(recipe_book):
    with open(recipe_book, 'r', encoding='utf-8') as recipes:
        result = {}
        for line in recipes:
            dish_name = line.strip()
            goods = []
            for item in range(int(recipes.readline())):
                ingridients = {}
                contents = recipes.readline().split(' | ')
                ingridients['ingridient_name'] = contents[0]
                ingridients['quantity'] = contents[1]
                ingridients['measure'] = contents[2].strip()
                goods.append(ingridients)
            result[dish_name] = goods
            recipes.readline()
        return result


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    cook_book = recipe_catalog(file_name)
    for dish in list(cook_book.keys()):
        if dish not in dishes:
            cook_book.pop(dish)

    for dish, ingridients in cook_book.items():
        for ingridient in ingridients:
            if list(ingridient.values())[0] not in result.keys():
                lib = {}
                lib[list(ingridient.keys())[2]] = list(ingridient.values())[2]
                lib[list(ingridient.keys())[1]] = int(list(ingridient.values())[1]) * person_count
                result[list(ingridient.values())[0]] = lib
            elif list(ingridient.values())[0] in result.keys():
                my_dict = result[list(ingridient.values())[0]]
                sum = (int(list(my_dict.values())[1] / person_count) + int(list(ingridient.values())[1])) * person_count
                lib = {}
                lib[list(ingridient.keys())[2]] = list(ingridient.values())[2]
                lib[list(ingridient.keys())[1]] = sum
                result[list(ingridient.values())[0]] = lib

    return result

pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))