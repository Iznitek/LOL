print("Привет")
a = int(input())
if a <= 18:
    print("Ты ещё маленький!")
elif a >= 18:
    print("Хочешь отгадаю дату твоего рождения?")
b = input()
if b == "да":
    print("1. Умнож на 2 число дня твоего рождения")
    print("2. До получившегося числа добавь 5")
    print("3. Умнож теперь это число на 50")
    print("4. Добавь номер месяца твоего рождения")
elif b != "да":
    print("Хорошо, до новых встреч!")

Recived_number = int(input())
Recived_number -= 250
Date = number // 100
Mount_number = number - 100*date
if Month_number == 1:
    Month_number = "Января"
    print("Твой день рождения: %s" %Date + Month_number)
elif Month_number == 2:
    Month_number = "Февраля"
    print("Твой день рождения: %s" %Date + Month_number)
elif Month_number == 3:
    Month_number = "Марта"
    print("Твой день рождения: %s" % Date + Month_number)
elif Month_number == 4:
    Month_number = "Апреля"
    print("Твой день рождения: %s" %Date + Month_number)
elif Month_number == 5:
    Month_number = "Мая"
    print("Твой день рождения: %s" %Date + Month_number)
elif Month_number == 6:
    Month_number = "Июня"
    print("Твой день рождения: %s" %Date + Month_number)
elif Month_number == 7:
    Month_number = "Июля"
    print("Твой день рождения: %s" %Date + Month_number)
elif Month_number == 8:
    Month_number = "Августа"
    print("Твой день рождения: %s" % Date + Month_number)
elif Month_number == 9:
    Month_number = "Сентября"
    print("Твой день рождения: %s" %Date + Month_number)
elif Month_number == 10:
    Month_number = "Октября"
    print("Твой день рождения: %s" %Date + Month_number)
elif Month_number == 11:
    Month_number = "Ноября"
    print("Твой день рождения: %s" %Date + Month_number)
elif Month_number == 12:
    Month_number = "Декабря"
    print("Твой день рождения: %s" %Date + Month_number)
else:

        print("Что то пошло не так!")

