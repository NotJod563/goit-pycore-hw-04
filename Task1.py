def total_salary(path):
    sum = 0
    overall_workers = 0
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            raw_string = file.read().replace("\n", ",") # Заміна перенесення рядку на кому, щоб далі ми могли виокремити цей те що між комами як окремий аргумент
            separated_string = raw_string.split(",") # Розділення рядку на аргументи по комі
            for argument in separated_string:
                if argument.isdigit(): # Перевірка аргументу на те що він число
                    sum = sum + int(argument) # Збільшення суми всіх аргументів
                    overall_workers += 1 # Збільшення дільнику для визначення середньої зарплатні
    except FileNotFoundError:
        print("Такого файлу не існує, файл не був зчитаним")
    if overall_workers != 0: # Перевірка існування робітників/зарплатні перед діленням на їх число
        median = int(sum/overall_workers)
        return sum, median
    else:
        return 0, 0


# Приклад використання:

# total, average = total_salary("Salary.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}") 
