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