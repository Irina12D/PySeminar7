# функция для первоначального ввода
def input_expression():
    expression = input("Готовы для вас вычислять. Введите выражение ")
    return expression

# функция для ввода числа - в случае, если идёт работа с одиночными операндами
def input_number():
     while True:
        try:
            number = int(input("Введите целое число "))
            return number
        except:
            print("Ошибка ввода!")

# функция для ввода арифметической операции - в случае, если идёт работа с одиночными операндами
def input_operation():
    while True:
        try:
            operation = input("Введите операцию ")
            if operation in ['+', '-', '*', '/', '='] and len(operation) == 1:
                return operation
        except:
            print("Введите корректную операцию")

# функция для вывода результата на экран
def print_to_console(text):
    print(text)

# функция для ввода прощального приветствия - завершение работы
def log_off():
    print('Всё посчитано. До свидания!')

# функция для ввода ошибки деления на ноль
def division_by_zero():
    print("Делить на ноль нельзя!")

# функция для ввода сообщения о неверном вводе (числа или выражения)
def invalid_expression():
    print("Неверный ввод!")