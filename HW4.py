
bad_report_string1 = ""
report_string1 = ""
number = number.replace('+', "").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

if len(number) == 11:
    report_string1 += "Длина номера верная\n"
else:
    bad_report_string1 += "Длина номера неверная\n"

if number.isdigit():
    report_string1 += "Номер состоит из цифр\n"
else:
    bad_report_string1 += "В номере телефона есть знаки, отличные от цифр\n"

if bad_report_string1:
    print(f'Ваш email не прошел проверку по следующим причинам:\n{bad_report_string1}')
else:
    print(f'Ваш номер телефона прошел проверку!\n{report_string1}')

password = input("Введите пароль: ")
THRESHOLD = 7
bad_report_string2 = ""
report_string2 = ""
SYMBOLS = ".,\"@!;:%:*()_-№?{}[]/\\"

if len(set(password) & set(SYMBOLS)):
    report_string2 += 'В пароле есть спецзнак\n'
else:
    bad_report_string2 += 'В пароле нет спецзнаков!\n'

if not 0 < password.lower().count(" ") < 2:
    report_string2 += f'В пароле нет пробелов\n'
else:
    bad_report_string2 += f'В пароле используется пробел!\n'

if not password.islower() and not password.isupper():
    report_string2 += 'Пароль содержит символы разных регистров\n'
else:
    bad_report_string2 += 'Пароль состоит из символов только одного регистра!\n'

if len(password) > THRESHOLD:
    report_string2 += "Длина пароля верная\n"
else:
    bad_report_string2 += "Длина пароля неверная!\n"

if bad_report_string2:
    print(f'Ваш email не прошел проверку по следующим причинам:\n{bad_report_string2}')
else:
    print(f'Ваш email прошел проверку!\n{report_string2}')