print("Привет")
print("Хочешь я у гадаю когда у тебя день рождения?")
choise = input()
if choise == "Да":
    print("Введи число от 1 до 12")
age = input()
if age >= "12":
    print("1. Умнож на 2 чмсло дня своего рождения")
    print("2. Теперь добавь 5")
    print("3. Умнож на 50")
    print("4. Добавь номер месяца своего рождения")
    print("Какое число ты получил?")
number = int(input())
number -= 250
date = number // 100
month = number - 100*date
if month == 1:
    month = "Января"
    print("Твоё день рождения: %s %s" %(date, month))
elif month == 2:
    month = "Февраля"
    print("Твоё день рождения: %s %s" %(date, month))
elif month == 3:
    month = "Марта"
    print("Твоё день рождения: %s %s" %(date, month))
elif month == 4:
    month = "Апреля"
    print("Твоё день рождения: %s %s" %(date, month))
elif month == 5:
    month = "Мая"
    print("Твоё день рождения: %s %s" %(date, month))
elif month == 6:
    month = "Июня"
    print("Твоё день рождения: %s %s" %(date, month))
elif month == 7:
    month = "Июля"
    print("Твоё день рождения: %s %s" %(date, month))
elif month == 8:
    month = "Августа"
    print("Твоё день рождения: %s %s" %(date, month))
elif month == 9:
    month = "Сентября"
    print("Твоё день рождения: %s %s" %(date, month))
elif month == 10:
    month = "Октября"
    print("Твоё день рождения: %s %s" %(date, month))
elif month == 11:
    month = "Ноября"
    print("Твоё день рождения: %s %s" %(date, month))
elif month == 12:
    month = "Декабря"
    print("Твоё день рождения: %s %s" %(date, month))
else:
    print("Что то пошло не так!")
