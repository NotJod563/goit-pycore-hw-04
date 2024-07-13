def get_cats_info(path):
    cat_list = []
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            cats = file.readlines()

            # Створення циклу для обробки кожного рядку
            for cat in cats:
                cat_info = cat.split(",")
                # Розбивка на словник
                cat_dict = {    
                    "id" : cat_info[0],
                    "name" : cat_info[1],
                    "age" : str(cat_info[2]).replace("\n", ""),
                }
                # Додавання словника до списку словників
                cat_list.append(cat_dict)

    except FileNotFoundError: # У випадку коли шлях не вірний, виводимо на екран повідомлення
        print("Такого файлу не існує, файл не був зчитаним")
    return cat_list

# Приклад використання:
# cats_info = get_cats_info("FilesForTasks\Cats.txt")
# print(cats_info)