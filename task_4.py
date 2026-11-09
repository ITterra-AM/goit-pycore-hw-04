def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Please write name and phone number."
    name, phone = args
    if name in contacts:
        return "Contact already exists, you can use 'change' command to update the phone number."
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Please write name and phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Please write the name of the contact."
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return "Contact not found."

def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    contact_list = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return f"All contacts:\n{contact_list}"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        elif command == "help":
            print("Available commands:")
            print("  hello - Greet the bot")
            print("  add <name> <phone> - Add a new contact")
            print("  change <name> <phone> - Change an existing contact's phone number")
            print("  phone <name> - Show the phone number of a contact")
            print("  all - Show all contacts")
            print("  help - Show available commands")
            print("  close/exit - Exit the program")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()