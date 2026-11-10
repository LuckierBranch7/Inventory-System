import os
from storage import Storage

storage = Storage()
inventory = storage.load()
get_quantity = 0
get_box = 1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_item(name, amount, box, inventory=inventory):
    if name in inventory:
        return f'{name} already exists.'

    inventory[name] = [amount, box]
    storage.save(inventory)
    return f'{name} has been added.'


def del_item(name, inventory=inventory):
    if not name in inventory:
        return f'{name} does not exist.'

    del inventory[name]
    storage.save(inventory)
    return f'{name} deleted.'


def add_quantity(name, amount, inventory=inventory):
    if not name in inventory:
        return f'{name} does not exist.'

    inventory[name][get_quantity] += amount
    storage.save(inventory)
    return f'{amount} {name}(s) added to inventory.'

def remove_quantity(name, amount, inventory=inventory):
    if not name in inventory:
        return f'{name} does not exist.'

    inventory[name][get_quantity] -= amount
    storage.save(inventory)
    return f'{amount} {name}(s) removed from inventory.'

def change_box(name, box, inventory=inventory):
    if not name in inventory:
        return f'{name} does not exist.'

    inventory[name][get_box] = box
    storage.save(inventory)
    return f'{name} moved to Box {box}'

def view_inventory(inventory=inventory):
    print('-------- Inventory --------')
    for item in inventory:
        print(f'Name: {item} | Quantity: {inventory[item][get_quantity]} | Box: {inventory[item][get_box]}')

def main():
    clear_screen()

    while True:
        print('-------- System ---------')
        print('1. Add Item')
        print('2. Delete Item')
        print('3. View Inventory')
        print('4. Add Quantity')
        print('5. Remove Quantity')
        print('6. Change Box')
        print('7. Exit\n')
        user_in = input('>>> ')

        try:
            user_in = int(user_in)
        except ValueError:
            clear_screen()
            print('Your input should be a number.\n')
            continue

        if user_in == 1:
            clear_screen()

            while True:
                name = input('Name of product: ')
                quantity = input('Quantity of product: ')
                box = input('Box product is in: ')

                if name in inventory:
                    clear_screen()
                    print(f'{name} already exists.\n')
                    break

                try:
                    quantity = int(quantity)
                except ValueError:
                    clear_screen()
                    print('Quantity should be a number.\n')
                    continue

                try:
                    add_item(name, quantity, box)
                    clear_screen()
                    print(f'{name} added to inventory.\n')
                    break
                except:
                    clear_screen()
                    print('Something went wrong.\n')
                    break
        elif user_in == 2:
            clear_screen()

            while True:
                name = input('Name of product: ')

                if not name in inventory:
                    clear_screen()
                    print(f'{name} does not exist.\n')
                    break

                try:
                    del_item(name)
                    clear_screen()
                    print(f'{name} deleted from inventory.\n')
                    break
                except:
                    clear_screen()
                    print('Something went wrong.\n')
                    break
        elif user_in == 3:
            clear_screen()
            view_inventory()
            print('\n')
            continue
        elif user_in == 4:
            clear_screen()

            while True:
                name = input('Name of product: ')
                amount = input('Amount to be added: ')

                if not name in inventory:
                    clear_screen()
                    print(f'{name} does not exist.\n')
                    break

                try:
                    amount = int(amount)
                except ValueError:
                    clear_screen()
                    print('Amount should be a number.\n')
                    continue

                try:
                    add_quantity(name, amount)
                    clear_screen()
                    print(f'{amount} {name}(s) added to inventory.\n')
                    break
                except:
                    clear_screen()
                    print('Something went wrong.\n')
                    break
        elif user_in == 5:
            clear_screen()

            while True:
                name = input('Name of product: ')
                amount = input('Amount to be removed: ')

                if not name in inventory:
                    clear_screen()
                    print(f'{name} does not exist.\n')
                    break

                try:
                    amount = int(amount)
                except ValueError:
                    clear_screen()
                    print('Amount should be a number.\n')
                    continue

                if amount < 0:
                    clear_screen()
                    print('Amount should be positive.')
                    continue

                try:
                    remove_quantity(name, amount)
                    clear_screen()
                    print(f'{amount} {name}(s) removed from inventory.\n')
                    break
                except:
                    clear_screen()
                    print('Something went wrong.\n')
                    break
        elif user_in == 6:
            clear_screen()

            while True:
                name = input('Name of product: ')
                box = input('Name of box: ')

                if not name in inventory:
                    clear_screen()
                    print(f'{name} does not exist.\n')
                    break

                try:
                    change_box(name, box)
                    clear_screen()
                    print(f'{name} moved to box {box}.\n')
                    break
                except:
                    clear_screen()
                    print('Something went wrong.\n')
                    break
        elif user_in == 7:
            clear_screen()
            print("Program has been closed.\n")
            break
        else:
            clear_screen()
            print('Input invalid. Pick an input between 1 and 7.\n')
            continue

main()