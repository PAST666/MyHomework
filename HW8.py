from data.cities import cities_list
empty_set = set()
empty_list = []
for i in cities_list:
    empty_set.add(i["name"].lower())
print(empty_set)
print(len(empty_set))
while len(empty_set) > 0:
    input_city = input("Введите название города:").lower()
    for element in empty_list:
        if input_city[0] != empty_list[-1][-1]:
            print("Вы ввели город, который начинается не на букву " + empty_list[-1][-1].upper())
            break
    print(input_city)
    if input_city in empty_set:
        empty_set.remove(input_city)
        print(len(empty_set))
        for city in empty_set:
            if city[0] == input_city[-1]:
                print(city)
                empty_list.append(city)
                empty_set.remove(city)
                print(len(empty_set))
                break
    else:
        print("Вы проиграли!")
        break

