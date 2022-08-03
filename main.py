def get_cook_book():
    with open('recipes.txt', encoding='utf-8') as file_object:
        cook_book = {}
        for line in file_object:
            dish_name = line.strip()
            ingredients_quantity = file_object.readline().strip()
            ingredients_list = []
            for i in range(int(ingredients_quantity)):
                name, quantity, measure = file_object.readline().strip().split(' | ')
                ingredients_list.append({'ingredient_name': name, 'quantity': int(quantity), 'measure': measure})
            cook_book[dish_name] = ingredients_list
            file_object.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
    shop_dict = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for recipe in cook_book[dish]:
                if recipe['ingredient_name'] in shop_dict:
                    shop_dict[recipe['ingredient_name']]['quantity'] += recipe['quantity'] * person_count
                else:
                    shop_dict[recipe['ingredient_name']] = {'measure': recipe['measure'], 'quantity': (recipe['quantity'] * person_count)}
        else:
            error = 'Блюдо не найдено'
            return error
    return shop_dict

