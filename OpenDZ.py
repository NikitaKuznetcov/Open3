from pprint import pprint


def cook_book(file_name):
    with open('recipes.txt', encoding='UTF-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            cook_book[dish_name] = []
            counter = int(file.readline().strip())
            for _ in range(counter):
                ingredient = file.readline().strip().split('|')
                temp_dict = {'имя ингредиента': ingredient[0], 'количество': ingredient[1], 'единица измерения': ingredient[2]}
                cook_book[dish_name].append(temp_dict)
            (file.readline())
        return cook_book

result = cook_book("recipes.txt")
pprint(result)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ing in cook_book('recipes.txt')[dish]:
            ing_name = ing["имя ингредиента"]
            if ing_name not in shop_list:
                shop_list[ing_name] = {"количество": int(ing["количество"]) * person_count, "единица измерения": ing["единица измерения"]}
            else:
                shop_list[ing_name]["количество"] += int(ing["количество"]) * person_count
    return shop_list

pprint(cook_book('recipes.txt'))
print()
pprint(get_shop_list_by_dishes(["Омлет", "Запеченный картофель"], 3))






