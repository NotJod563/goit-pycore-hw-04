def parse_input(user_input):  
    cmd, *args = user_input.split() # Розділяємо введений рядок на команду та аргументи
    cmd = cmd.strip().lower() # Перетворюємо команду в нижній регістр
    return cmd, *args

def add_contact(args, contacts): # Додаємо контакт до словника
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts): # Оновлюємо номер телефону для існуючого контакту
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def show_phone(args,contacts): # Виводимо номер телефону для зазначеного контакту
    phone_number = contacts.get(args)
    return phone_number


def main():
    contacts = {} # Словник для збереження контактів
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "phone":
            print(show_phone(args[0],contacts))
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()