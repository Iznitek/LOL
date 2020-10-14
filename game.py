import random
import time
score = 0
print("Привет, меня зовут Б.О.Т. я создан для того")
print("чтобы научить тебя играть в эту игру.")
time.sleep(2)
print("Ну что приступим?")
answer = input()
if answer == "да":
    print("Правила игры:")
    print("Я буду задавать тебе вопросы ")
    print("и говорить варианты ответов а ты должен выбирать ")
    print("от твоего выбора зависят дальнейшие события.")
    time.sleep(1)
    print("Понятны правила?")
    rules = input()
    if rules == "да":
        print("Привет")
        time.sleep(1)
        print("Варианты: 1 - Привет, 2 - Пока")
        a1 = int(input())
        if a1 == 1:
            print("Как тебя зовут?")
            time.sleep(1)
            print("Варианты: Назвать своё имя ")
            score += 1
            a2 = input()
            if a2 != 1:
                print("%s - Класное имя " %a2)
                time.sleep(1)
                print("Меня зовут Артём. Давай дружить?")
                time.sleep(1)
                print("Варианты: 1 - Нет, 2 - Да, 3 - Я подумаю")
                score += 1
                a3 = int(input())
                if a3 == 1:
                    print("Хорошо, пока")
                    time.sleep(1)
                    print("Вы проиграли!")
                    print("Поздравляем вы заработали %s балла " % score)
                elif a3 == 3:
                    score += 0.5
                    print("Думай Быстрее...")
                    time.sleep(1)
                    print("Вы проиграли!")
                    print("Поздравляем вы заработали %s балла " % score)
                    print("* Вы получили Достижение - Быстрее думай! *")
                elif a3 == 2:
                    score += 2
                    print("Урааа!!")
                    time.sleep(1)
                    print("А что ты больше любишь?")
                    time.sleep(1)
                    print("Варианты: 1 - Футбол, 2 - Школу, 3 - Себя, 4 - Тебя, 5 - Маму")
                    a4 = int(input())
                    if a4 == 1:
                        print("А я не люблю!")
                        time.sleep(1)
                        print("Вы проиграли!")
                        print("Поздравляем вы заработали %s балла " % score)
                    elif a4 == 2:
                        score += 0.5
                        print("КАК???!?!?!?!?")
                        time.sleep(1)
                        print("Вы проиграли!")
                        print("Поздравляем вы заработали %s балла " % score)
                        time.sleep(1)
                        print("* Вы получили Достижение - Ты не человек!!! *")
                    elif a4 == 3:
                        print("Ты какой то самовлюблённый!")
                        time.sleep(1)
                        print("Вы проиграли!")
                        print("Поздравляем вы заработали %s балла " % score)
                    elif a4 == 4:
                        print("Я с такими не общаюсь!!")
                        time.sleep(1)
                        print("~~Артём покинул чат~~")
                        time.sleep(1)
                        print("Вы проиграли!")
                        print("Поздравляем вы заработали %s балла " % score)
                        time.sleep(1)
                        print("* Вы получили Достижение - Иди отсюда^_^ *")
                    elif a4 == 5:
                        score += 2
                        print("Я тоже, хоть в где-то мы сошлись во мнении...")
                        time.sleep(1)
                        print("Варианты: 1 - Нет, 2 - Любишь майн?, 3 - Любишь кс-го?")
                        a5 = int(input())
                        if a5 == 1:
                            score += 0.5
                            print("Что значит нет?")
                            time.sleep(1)
                            print("Вы проиграли!")
                            print("Поздравляем вы заработали %s балла " % score)
                        elif a5 == 2:
                            score += 9999999
                            print("МАЙНКРААААААААААААААААААААААААФТ")
                            time.sleep(1)
                            print("~~Артём сошёл с ума~~")
                            time.sleep(1)
                            print("*Вы получили 9999999 баллов!*")
                            time.sleep(1)
                            print("Вы проиграли!")
                            print("Поздравляем вы заработали %s балла " % score)
                            time.sleep(1)
                            print("* Вы получили Достижение - !Майнкрафтер! *")
                        elif a5 == 3:
                            score += 2
                            print("Да")
                            time.sleep(1)
                            print("Как тебе матч NAVI против Virtus Pro???")
                            time.sleep(1)
                            print("Варианты: 1 - Да, 2 - Нет, 3 - Мне очень понравилось как s1mple сделал эйс!")
                            a6 = int(input())
                            if a6 == 1:
                                print("Тебе понравился прострел на миду от симпла?")
                                time.sleep(1)
                                print("Варианты: 1 - Да")
                                f = int(input())
                                if f == 1:
                                    score -= 642984748
                                    print("Врун, там небыло никаких прострелов!!!")
                                    time.sleep(1)
                                    print("Вы проиграли!")
                                    print("Поздравляем вы заработали %s балла " % score)
                                    time.sleep(1)
                                    print("* Вы получили Достижение - Врёшь и не краснеешь... *")
                                else:
                                    print("Вы проиграли!")
                                    print("Поздравляем вы заработали %s балла " % score)
                            elif a6 == 2:
                                score -= 747368713
                                print("Вы проиграли!")
                                print("Поздравляем вы заработали %s балла " % score)
                            elif a6 == 3:
                                score += 3
                                print("Спасибо за прохождение моей игры!!!!")
                                time.sleep(1)
                                print("Вы заработали %s балла " % score)
                                time.sleep(1)
                                print("* Вы получили Достижение - Спасибо! *")
                            else:
                                print("Вы проиграли!")
                                print("Поздравляем вы заработали %s балла " % score)
                        else:
                            print("Вы проиграли!")
                            print("Поздравляем вы заработали %s балла " % score)
                    else:
                        print("Вы проиграли!")
                        print("Поздравляем вы заработали %s балла " % score)
                else:
                    print("Вы проиграли!")
                    print("Поздравляем вы заработали %s балла " % score)
            elif a2 == 1:
                print("Ну как хочешь!")
                time.sleep(2)
                print("Вы проиграли!")
                print("Поздравляем вы заработали %s балла " %score)
            else:
                print("Вы проиграли!")
                print("Поздравляем вы заработали %s балла " % score)
        elif a1 == 2:
            print("Зачем так грубо?")
            time.sleep(1)
            print("Варианты: 1 - Потому что так хочу, 2 - Прости.")
            a2 = input()
            if a2 == 1:
                print("Вы проиграли!")
                print("Поздравляем вы заработали %s балла " %score)
            else:
                print("Вы проиграли!")
                print("Поздравляем вы заработали %s балла " %score)
        else:
            print("Вы проиграли!")
            print("Поздравляем вы заработали %s балла " %score)
    elif rules == "нет":
        print("Хорошо, пока.")
    else:
        print("Извини мне не удалось обработать твой ответ.")
elif answer == "нет":
    print("Хорошо, пока.")
elif answer == "yes":
    time.sleep(1)
    print("* Вы получили Достижение - Do you speak english??? *")
else:
    print("Извини мне не удалось обработать твой ответ.")
