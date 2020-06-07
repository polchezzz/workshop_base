def print_start_menu():
    print('[1] Catalog')
    print('[2] Storage')
    print('[3] Exit')

    while True:
        try:
            option = int(input('Please, enter your option: '))
            if option < 1 or option > 3:
                print('Incorrect option! Try again!')
            else:
                return option
        except ValueError:
            print('Option is not a number!')


def print_storage_menu():
    print('[1] View all materials')
    print('[2] Add material')
    print('[3] Available workshops')
    print('[4] Activate workshop')
    print('[5] Deactivate workshop')
    print('[6] Add money to budget')
    print('[7] Change extra charge')
    print('[8] Back')

    while True:
        try:
            option = int(input('Please, enter your option: '))
            if option < 1 or option > 8:
                print('Incorrect option! Try again!')
            else:
                return option
        except ValueError:
            print('Option is not a number!')


def print_catalog_menu():
    print('[1] View all')
    print('[2] Back')

    while True:
        try:
            option = int(input('Please, enter your option: '))
            if option < 1 or option > 2:
                print('Incorrect option! Try again!')
            else:
                return option
        except ValueError:
            print('Option is not a number!')
