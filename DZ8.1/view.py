
def main_menu():
    commands = ['Открыть файл',
                'Сохранить файл',
                'Показать контакты',
                'Добавить контакт',
                'Найти контакт',
                'Изменить контакт',
                'Удалить контакт',
                'Выйти из программы']
    print('\nВыберите пункт меню: ')
    for i in range(len(commands)):
        print(f'\t{i+1}. {commands[i]}')
    user_input = int(input('\nВведите пункт меню: '))
    return user_input

def show_contacts(phone_book: list):
    if len(phone_book) > 0:
        for item in phone_book:
            print(f'{item[0]} {item[1]} ({item[2]})')
    else:
        print('Телефонная книга пуста или не загружена.')

def load_success():
    print('Телефонная книга успешно загружена')

def save_success():
    print('Телефонная книга сохранена успешно')

def delete_succes():
    print('Контакт успешно удален')

def change_succes():
    print('Контакт успешно изменен')

def new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий к контакту: ')
    return name, phone, comment

def find_contact():
    search = input('Введите искомое значение: ')
    return search

def delete_contact():
    j = int(input('\nВведите номер контакта, который хотите удалить: '))
    return j

def change_contact():
    j = int(input('\nВведите номер контакта, который хотите изменить: '))
    return j