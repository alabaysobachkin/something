a = input('Хотите ли вы приступить? ')
s = 0
if a == 'да' or a == 'yes' or a == 'Да' or a == 'Yes' or a == 'YES' or a == 'ДА':
    print(' Приступим!')
    f = open('task1.txt', 'r')
    print(*f)
    v = float(input('Введите ответ: '))
    if v == 2:
        s += 1
        print("правильно")
    else:
        print("Неправильно")
    print("идем дальше!")
    f = open('task2.txt', 'r')
    print(*f)
    v = float(input('Введите ответ: '))
    if v == 12 or v == 21:
        s += 1
        print("Все именно так!")
        print("не сбовляем темп и двигаемся вперед!")
    else:
        print("нет ты ошибся. o(╥﹏╥)o")
        print("ну ничего постарайся ответить на следующий вопрос")
    f = open('task3.txt', 'r')
    print(*f)
    v = float(input('Введите ответ: '))
    if v == 1.2:
        s += 1
        print("отлично!")
        print("еще остались вопросы, пошли!")
    else:
        print("как так. ")
        print("у тебя еще есть шансы проявить себя")
    f = open('task4.txt', 'r')
    print(*f)
    v = float(input('Введите ответ: '))
    if v == 80:
        s += 1
        print("потрясающе!")
        print("следующий вопрос")
    else:
        print("соберись. ")
    f = open('task5.txt', 'r')
    print(*f)
    v = float(input('Введите ответ: '))
    if v == 18.2:
        s += 1
    else:
        print("неправильно")

else:
    print('Важно иметь желание!')
print("что же это был последний вопрос. сейчас посчитаем баллы и поставим оценку")
if s == 5:
    print("ВАУ, это восхитительно, у тебя ", s, "баллов и оценка 5")
elif s == 4:
    print("Молодец, у тебя ", s, "баллов и оценка 4")
elif s == 3:
    print("сойдет,", s, "баллов и оценка 3")
else:
    print(s, "баллов и оценка 3")
