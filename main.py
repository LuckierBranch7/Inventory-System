import os
import functions as fs
from storage import Storage

storage = Storage()
inventory = storage.load()
get_quantity = 0
get_box = 1

def main():
    fs.clear_screen()

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
            fs.clear_screen()
            print('Your input should be a number.\n')
            continue

        if user_in == 1:
            fs.clear_screen()

            while True:
                name = input('Name of product: ')
                quantity = input('Quantity of product: ')
                box = input('Box product is in: ')

                if name in inventory:
                    fs.clear_screen()
                    print(f'{name} already exists.\n')
                    break

                try:
                    quantity = int(quantity)
                except ValueError:
                    fs.clear_screen()
                    print('Quantity should be a number.\n')
                    continue

                try:
                    fs.add_item(name, quantity, box)
                    fs.clear_screen()
                    print(f'{name} added to inventory.\n')
                    break
                except:
                    fs.clear_screen()
                    print('Something went wrong.\n')
                    break
        elif user_in == 2:
            fs.clear_screen()

            while True:
                name = input('Name of product: ')

                if not name in inventory:
                    fs.clear_screen()
                    print(f'{name} does not exist.\n')
                    break

                try:
                    fs.del_item(name)
                    fs.clear_screen()
                    print(f'{name} deleted from inventory.\n')
                    break
                except:
                    fs.clear_screen()
                    print('Something went wrong.\n')
                    break
        elif user_in == 3:
            fs.clear_screen()
            fs.view_inventory()
            print('\n')
            continue
        elif user_in == 4:
            fs.clear_screen()

            while True:
                name = input('Name of product: ')
                amount = input('Amount to be added: ')

                if not name in inventory:
                    fs.clear_screen()
                    print(f'{name} does not exist.\n')
                    break

                try:
                    amount = int(amount)
                except ValueError:
                    fs.clear_screen()
                    print('Amount should be a number.\n')
                    continue

                try:
                    fs.add_quantity(name, amount)
                    fs.clear_screen()
                    print(f'{amount} {name}(s) added to inventory.\n')
                    break
                except:
                    fs.clear_screen()
                    print('Something went wrong.\n')
                    break
        elif user_in == 5:
            fs.clear_screen()

            while True:
                name = input('Name of product: ')
                amount = input('Amount to be removed: ')

                if not name in inventory:
                    fs.clear_screen()
                    print(f'{name} does not exist.\n')
                    break

                try:
                    amount = int(amount)
                except ValueError:
                    fs.clear_screen()
                    print('Amount should be a number.\n')
                    continue

                if amount < 0:
                    fs.clear_screen()
                    print('Amount should be positive.')
                    continue

                try:
                    fs.remove_quantity(name, amount)
                    fs.clear_screen()
                    print(f'{amount} {name}(s) removed from inventory.\n')
                    break
                except:
                    fs.clear_screen()
                    print('Something went wrong.\n')
                    break
        elif user_in == 6:
            fs.clear_screen()

            while True:
                name = input('Name of product: ')
                box = input('Name of box: ')

                if not name in inventory:
                    fs.clear_screen()
                    print(f'{name} does not exist.\n')
                    break

                try:
                    fs.change_box(name, box)
                    fs.clear_screen()
                    print(f'{name} moved to box {box}.\n')
                    break
                except:
                    fs.clear_screen()
                    print('Something went wrong.\n')
                    break
        elif user_in == 7:
            fs.clear_screen()
            print("Program has been closed.\n")
            break
        else:
            fs.clear_screen()
            print('Input invalid. Pick an input between 1 and 7.\n')
            continue

main()