from classes.catalog import Catalog
from classes.files import *
from classes.info import *
from classes.storage import *


storage_info_path = "data/storage/Info.txt"
storage_materials_path = "data/storage/materials.txt"
storage_active_workshops_path = "data/storage/active"
catalog_path = "data/catalog/"


def main():

    catalog = Catalog()


    try:
        storage = read_storage(storage_info_path)
        read_materials(storage_materials_path, storage)
        read_active_workshops(storage_active_workshops_path, storage)
        read_workshops(catalog_path, catalog)
    except Exception:
        print('Problems with files. Check that they are correct!')
        return

    option = print_start_menu()

    while option != 3:
        if option == 1:
            catalog_option = print_catalog_menu()
            print()

            while catalog_option != 2:
                if catalog_option == 1:
                    print(catalog)
                catalog_option = print_catalog_menu()

        if option == 2:
            storage_option = print_storage_menu()
            print()

            while storage_option != 8:
                if storage_option == 1:
                    print(storage)

                if storage_option == 2:
                    name = input("Enter name: ")
                    amount = get_int("Enter amount: ", False)
                    price = get_int("Enter price: ", False)
                    renewable = get_int("Enter 1, if renewable, or 0 instead: ", True)

                    print(storage.add_material(Material(name, amount, price, renewable)))
                    print()
                    write_materials(storage_materials_path, storage.materials)

                if storage_option == 3:
                    print(storage.find_workshops(catalog))
                    print()

                if storage_option == 4:

                    name = input("Enter workshop name (not full name): ")
                    workshop = find_workshop(catalog, name)

                    if not workshop:
                        print("Workshop with such name not found!")
                    else:
                        flag, message = storage.add_workshop(workshop)
                        print(message)
                        print()
                        if flag:
                            write_workshop(storage_active_workshops_path, workshop)
                            write_materials(storage_materials_path, storage.materials)

                if storage_option == 5:
                    name = input("Enter workshop name (not full name): ")
                    workshop = find_workshop(catalog, name)

                    if not workshop:
                        print("Workshop with such name not found!")
                    else:
                        flag, message = storage.delete_workshop(workshop)
                        print(message)
                        print()
                        if flag:
                            remove_active_workshop(storage_active_workshops_path, workshop.name)
                            write_materials(storage_materials_path, storage.materials)

                if storage_option == 6:
                    money = get_int("Enter amount of money (positive number): ", False)
                    print(storage.add_budget(money))
                    print()
                    write_storage(storage_info_path, storage)

                if storage_option == 7:
                    extra = get_int("Enter extra charge value (positive number): ", False)
                    print(storage.change_extra(extra))
                    print()
                    write_storage(storage_info_path, storage)

                storage_option = print_storage_menu()

        option = print_start_menu()


def get_int(message, flag):

    while True:
        temp = input(message)
        try:
            temp = int(temp)
            if not flag:
                return temp
            elif (temp == 0) or (temp == 1):
                return temp
            else:
                print("Can't cast to bool!")
        except ValueError:
            print("Not a number! Try again!")


def find_workshop(catalog, name):

    for workshop in catalog.workshops:
        if workshop.name == name:
            return workshop
    return None



if __name__ == '__main__':
    main()
