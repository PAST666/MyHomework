data_lst = ['1', '2', '3', '4d', 5]
list1 = []
for i in data_lst:
    try:
        i = int(i)
        list1.append(i)
    except ValueError:
        print(f"Вы ввели значение {i}, которое не является числом!")
print(list1)

nums = input("Введите номера телефонов через точку с запятой (без пробелов):")
nums = nums.split(";")
# nums = ['+77053183958', '+77773183958', '87773183958',
#         '+(777)73183958', '+7(777)-731-83-58', '+7(777) 731 83 58', '896594209444']
for i in nums:
    i = i.replace("+", "").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    if len(i) != 11:
        raise ValueError(f'Длина номера {i} не равна 11 знакам')
    if not (i[0] != 7 or i[0] != 8):
            raise ValueError(f'Номер {i} начинается не с цифры 8')
    if not i.isdigit():
        raise ValueError(f'В номере {i} есть недопустимые знаки')