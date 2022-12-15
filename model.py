import OPN

number1 = 0
number2 = 0
operation = ''
formula = ''
result = 0

# функция для возврата значения первого операнда в одиночных вычислениях
def get_first():
    global number1
    return number1

# функция для возврата значения второго операнда в одиночных вычислениях
def get_second():
    global number2
    return number2

# функция для возврата значения арифметической операции в одиночных вычислениях
def get_operation():
    global operation
    return operation

# функция для возврата арифметического выражения, заданного формулой
def get_formula():
    global formula
    return formula

# функция для возврата результата вычислений
def get_result():
    global result
    return result

# функция для задания значения первого операнда в одиночных вычислениях
def set_first(value):
    global number1
    number1 = value

# функция для задания значения второго операнда в одиночных вычислениях
def set_second(value):
    global number2
    number2 = value

# функция для задания значения арифметической операции в одиночных вычислениях
def set_operation(value):
    global operation
    operation = value

# функция для задания значения арифметического выражения, заданного формулой
def set_formula(value):
    global formula
    formula = value

# функция для выполнения сложения в одиночных вычислениях
def addition():
    global number1
    global number2
    global result
    result = number1 + number2

# функция для выполнения вычитания в одиночных вычислениях
def subtraction():
    global number1
    global number2
    global result
    result = number1 - number2

# функция для выполнения умножения в одиночных вычислениях
def multiplication():
    global number1
    global number2
    global result
    result = number1 * number2
    if result == int(result):
        result = int(result)

# функция для выполнения деления в одиночных вычислениях
def division():
    global number1
    global number2
    global result
    result = number1 / number2
    if result == int(result):
        result = int(result)

# функция для выполнения вычислений выражения, заданного формулой
# (основано на представлении формулы в постфиксной нотации)
def calc():
    global result
    result = OPN.calculation(OPN.postfix_notation(get_formula()))

