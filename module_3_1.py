calls = 0
list_ = []
control = True
n = 0
m = 0
string = ''
string_search = ''
str = ''

def count_calls():
    global calls
    calls = calls + 1
    return(calls)

def string_info(string):
    count_calls()
    len_ = len(string)
    a = string.upper()
    b = string.lower()
    string = (len_, a, b)
    return(string)

def is_contains(string_search, list_):
    count_calls()
    global control
    string_search = string_search.lower()
    for i in range(len(list_)):
        list_[i] = list_[i].lower()
        if string_search == list_[i]:
            control = True
            break
        else:
            control = False
    return(control)

print('Добро пожаловать!')
print('-----------------')
name = input('Как Вас зовут? ')
print('Здравствуйте, ', name)
while n != 4:
    print('Выберите действие:')
    print('1. Разбор слова.')
    print('2. Проверка слова в списке.')
    print('3. Сколько раз использовались функции.')
    print('4. Выход')
    n = input()
    if n == '1':
        print('Введите слово: ')
        print(string_info(input(string)))
    elif n == '2':
        print('Введите слово, которое ищем: ')
        string_search = input(string_search)
        print('Создайте список: ')
        while m == 0:
            print('Для завершения напишите stop')
            str = input('Введите элемент списка: ')
            if str == 'stop' or str == 'Stop' or str == 'STOP':
                break
            list_.append(str)
        print(is_contains(string_search, list_))
    elif n == '3':
        print('Количество вызовов функций: ', calls)
    else:
        break
print('До свидания, ', name)
