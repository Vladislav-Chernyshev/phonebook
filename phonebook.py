# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller

import os


def get_user_data() -> list:
    name = input('Введите имя: ')
    sur_name = input('Введите фамилию: ')
    phone = input('Введите телефон: ')
    desc = input('Введите описание: ')
    return [name, sur_name, phone, desc]


def create(gb_phone_book: list, user_data: list) -> list:
    gb_phone_book.append(user_data)
    return gb_phone_book


def find_user(gb_phone_book: list) -> list:
    sur_name = input('Введите фамилию для поиска: ').lower()
    for user in gb_phone_book:
        if user[0].lower().startswith(sur_name):
            print(f'По вашему запросу найдена запись: {user}\n')
            return user
    else:
        print('Такого человека нет в справочнике')


def update(gb_phone_book: list) -> list:
    ind = gb_phone_book.index(find_user(gb_phone_book))
    gb_phone_book[ind] = get_user_data()
    print(f'Данные обновлены на {gb_phone_book[ind]}\n')
    return gb_phone_book


def delete(gb_phone_book: list) -> list:
    user = find_user(gb_phone_book)
    if user is not None:
        gb_phone_book.remove(user)
        print(f'Запись {user} удалена.\n')
        return gb_phone_book


def print_phone_book(gb_phone_book: list) -> None:
    for user in gb_phone_book:
        print(user)


def get_file_name() -> str:
    return input('Введите название файла: ')


def import_data(gb_phone_book: list, file_name: str, delimiter: str) -> list:
    path_source = os.path.join('.', file_name)
    with open(path_source, 'r', encoding='utf-8') as source:
        for line in source:
            gb_phone_book = create(gb_phone_book, line.strip().split(delimiter))
        print(f'Данные импортированы из файла {file_name}\n')
    return gb_phone_book


def export_data(gb_phone_book: list, file_name: str, delimiter: str):
    path_source = os.path.join('.', file_name)
    with open(path_source, 'w', encoding='utf-8') as source:
        for line in gb_phone_book:
            user = f'{line[0]}{delimiter}{line[1]}{delimiter}{line[2]}{delimiter}{line[3]}\n'
            source.write(user)
        print(f'Данные экспортированы в файл {file_name}\n')


def menu():
    phone_book = list()
    while True:
        choice = int(input(
            'Выберите пункт меню:\n1. Выход\n2. Создать запись\n3. Найти пользователя\n4. Изменить запись\n5. Удалить '
            'запись\n6. Показать справочник\n7. Импорт данных\n8. Экспорт данных\nВыбор: '))
        if choice == 1:
            print('Вы выбрали выход!')
            return 0
        elif choice == 2:
            phone_book = create(phone_book, get_user_data())
        elif choice == 3:
            find_user(phone_book)
        elif choice == 4:
            update(phone_book)
        elif choice == 5:
            delete(phone_book)
        elif choice == 6:
            print_phone_book(phone_book)
        elif choice == 7:
            phone_book = import_data(phone_book, get_file_name(), ',')
        elif choice == 8:
            export_data(phone_book, get_file_name(), ',')
        else:
            print('Выбран некорректный пункт меню!\n')


menu()
