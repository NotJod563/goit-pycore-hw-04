import sys
from pathlib import Path
from colorama import Fore, Style

def print_colored(text, color): # Робимо як нас вчить принцип DRY, тобто виводимо все що повторюється в окремий метод
    print(f"{color}{text}{Style.RESET_ALL}")

def files_and_subdirs(directory, indent=""):
    try:
        path = Path(directory)
        if not path.exists(): #Перевірка існування шляху
            print("Такого файлу або шляху не існує")
            return
        
        if path.is_dir():
            print_colored(f"{indent} {path.name}/", Fore.BLUE)  # Вивід кореневої папки
            for item in path.iterdir():
                if item.is_dir():
                    files_and_subdirs(item, indent + " ") # Рекурсивний виклик зі збільшеним відступом
                else:
                    print_colored(f"{indent}  {item.name}", Fore.GREEN) # Відображення файлу
        else:
            print_colored(f"{indent} {path.name}", Fore.GREEN)  # Відображення файлу
    except Exception:
        print("Error happened")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Використовуйте: python Task3.py </шлях/до/вашої/директорії!>")
        sys.exit(1)

    directory_path = sys.argv[1]
    files_and_subdirs(directory_path)