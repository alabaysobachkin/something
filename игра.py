a = input('Хотите ли вы приступить? ')
N = 1
with open('answers.txt') as file:
    answer = file.readlines(N)
b = None
if a == 'да' or a == 'yes' or a == 'Да' or a == 'Yes' or a == 'YES' or a == 'ДА':
    print(' Приступим!')
    f = open('task1.txt', 'r')
    print(*f)
    input('Введите ответ: ')
    b = 1
    N += 1
else:
    print('Важно иметь желание!')
print (b)