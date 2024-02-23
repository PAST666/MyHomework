inputphrase = input("Введите слово или фразу: ")
inputphraselower = inputphrase.lower().replace(" ", "")
inputphraseback = inputphraselower[::-1]
if inputphraselower == inputphraseback:
    print(f'Обнаружен палиндром {inputphrase}')
else:
    print("Введенный текст не является палиндромом.")