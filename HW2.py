count = int(input("Введите количество секунд: "))
hours = int(count // 3600)
remain = count % 3600
minutes = int(remain / 60)
seconds = remain % 60
print(f"В указанном количестве секунд ({count}):\n"
      f"Часов: {hours}\n"
      f"Минут: {minutes}\n"
      f"Секунд: {seconds}")
countDegrees = int(input("Введите температуру в градусах Цельсия: "))
calvinDegrees = round(countDegrees * 274.15, 2)
farengDegrees = round(countDegrees * 33.8, 2)
reomurDegrees = round(countDegrees * 0.8, 2)
print(f"В указанном количестве градусов цельсия: {countDegrees}:\n"
      f"Градусов Кельвина: {calvinDegrees}\n"
      f"Градусов Фаренгейта: {farengDegrees}\n"
      f"Градусов Реомюра: {reomurDegrees}"
      )