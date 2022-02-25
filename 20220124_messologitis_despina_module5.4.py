import random
import os

ITEMS_FILENAME = "wizard_all_items.txt"
INVENTORY_FILENAME = "wizard_inventory.txt"

items_list = ["a wooden staff", "a wizard hat", "a cloak of invisibility", "some elven bread", "an unknown potion",
                  "a scroll of uncursing", "a scroll of invisibility", "a crossbow", "a wizard's cloak"]


def read_items():
    items = []
    with open(ITEMS_FILENAME, 'w') as file:
        for i in items_list:
            file.write(i + '\n')
    with open(ITEMS_FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            items.append(line)
    return items


def read_inventory():
    inventory = []

    try:
        with open(INVENTORY_FILENAME) as file:
            for line in file:
                line = line.replace("\n", "")
                inventory.append(line)
        return inventory
    except FileNotFoundError:
        print('Could not find inventory file!\nWizard is starting with no inventory.\n')
        with open(INVENTORY_FILENAME, 'w') as file:
            pass
        return inventory


def write_inventory(inventory):
    with open(INVENTORY_FILENAME, "w") as file:
        for item in inventory:
            file.write(item + "\n")


def display_title():
    print("The Wizard Inventory program")
    print()


def display_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()


def walk(inventory):
    items = read_items()
    item = random.choice(items)
    print("While walking down a path, you see " + item + ".")
    choice = input("Do you want to grab it? (y/n): ")
    choice = choice.lower()
    choice = choice.strip()
    if choice == "y":
        if len(inventory) >= 4:
            print("You can't carry any more items. " +
                  "Drop something first.\n")
        else:
            inventory.append(item)
            print("You picked up " + item + ".\n")
            write_inventory(inventory)
    elif choice == "n":
        print("Bummer you didn't snag", item + ".\n")
    else:
        print("Oh no! You didn't select y/n, last chance for", item)
        choice = input("Do you want to grab it? (y/n): ")
        choice = choice.lower()
        choice = choice.strip()
        if choice == "y":
            if len(inventory) >= 4:
                print("You can't carry any more items. " +
                      "Drop something first.\n")
            else:
                inventory.append(item)
                print("You picked up " + item + ".\n")
                write_inventory(inventory)
        else:
            print("Bummer you didn't snag", item + ".\n")

def show(inventory):
    try:
        if len(inventory) == 0:
            print('Yikes, no inventory yet!\nTry taking a WALK to get some items for your journey.\n')
        else:
            for i in range(len(inventory)):
                item = inventory[i]
                number = i + 1
                print(str(number) + ". " + item)
                print()
    except TypeError:
        print('Yikes, no inventory yet!\nTry taking a WALK to get some items for your journey.\n')

def drop_item(inventory):
    try:
        if len(inventory) == 0:
            print('No inventory available to drop.\n')
        else:
            number = input("Number: ")
            try:
                number = int(number)
                if number < 1 or number > len(inventory):
                    print("Invalid item number.\n")
                else:
                    item = inventory.pop(number - 1)
                    print("You dropped " + item + ".\n")
                    write_inventory(inventory)
            except ValueError:
                print("Whoops! That's not a number!\n")
    except TypeError:
        print('No inventory available to drop.\n')

def main():
    display_title()
    display_menu()

    inventory = read_inventory()

    while True:
        command = input("Command: ")
        command = command.lower()
        command = command.strip()
        if command == "walk":
            walk(inventory)
        elif command == "show":
            show(inventory)
        elif command == "drop":
            drop_item(inventory)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


if __name__ == "__main__":
    main()