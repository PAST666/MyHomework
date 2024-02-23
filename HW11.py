""""
Документация модуля
Игра в города
Пользователь и компьютер поочередно вводят названия городов, которые заканчиваются на последнюю букву
Функции:
1. Формирование множества городов
2. Формирование множества уникальных букв
3. Формирование множества плохих букв
4. Функция main() - точка входа в программу
5.



"""
from data.cities import cities_list
bad_letters_set = set()
def get_cities_set(cities_list: str) -> set:
    """
    Функция, которая принимает список городов и возвращает множество городов,
    : param cities_list : список городов,
    : return : множество городов
    """
    return {city['name'] for city in cities_list}
def get_unique_letters_set(cities_set: set) -> set:
    """
    Функция, которая принимает множество городов и возвращает множество уникальных букв и символов,
    : param cities_list : список городов,
    : return : множество уникальных букв и символов
    """
    return set(''.join(cities_set).lower())
def get_bad_letters_set(letter: str) -> set:
    """
    Функция, которая принимает букву и возвращает множество "плохих" букв,
    : param letter : буква,
    : return : множество "плохих" букв
    """
    return bad_letters_set.add(letter)
def main():
    """
    Точка входа в программу
    :return: None
    """

    cities_set = get_cities_set(cities_list)
    # cities_set = {city['name'].title() for city in cities_list}
    # print(cities_set)
    iter_count = 0
    # bad_letters_set = set()


    unique_letters_set = get_unique_letters_set(cities_set)

    # print(f'{unique_letters_set=}')


    for letter in unique_letters_set:
        for city in cities_set:
            if city[0].lower() == letter:
                break
    else:
        get_bad_letters_set(letter)
    computer_city = None
    while True:
        user_city = input('Введите название города:').strip().title()
        if user_city == '0':
            print('Вы сдались, до свидания!')
            break
        if user_city not in cities_set:
            print('Такого города нет!')
            break
        if computer_city:
            if user_city[0].lower() != computer_city[-1].lower():
                print('Не та буква!')
                break
        def remove_user_city(user_city):
            return cities_set.remove(user_city)
        remove_user_city(user_city)

        last_user_letter = user_city[-1]

        for city in cities_set:
            if city[0].lower() == last_user_letter:
                if city[-1].lower() in bad_letters_set:
                    continue
                def remove_cities_set(city):
                    return cities_set.remove(city)
                remove_cities_set(city)
                print(f'Компьютер:{city}')
                computer_city = city
                break
        else:
            print('Ты выиграл!')
            break
        for city in cities_set:
            if city[0].lower() == last_user_letter:
                def remove_cities_set(city):
                    return cities_set.remove(city)
                remove_cities_set(city)
                # print(city)
                computer_city = city
                break
        else:
            print("Ты выиграл!")
            break
main()