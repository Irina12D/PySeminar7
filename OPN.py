# функции для работы с Обратной Польской Записью

# функция для приведения выражения к удобному виду (для разбивки по слагаемым и операциям)
def expression_members(expression):
    new_expression = ' '
    for i in range(len(expression)):
        if expression[i].isdigit() or expression[i] == ' ' and expression[i-1] != ' ':
            new_expression += expression[i]
        elif expression[i] in '+-*/()':
            if expression[i-1] != ' ' and new_expression[-1] != ' ':
                new_expression += ' '
            new_expression += expression[i]
            if i < len(expression)-1 and expression[i + 1] != ' ' and new_expression[-1] != ' ':
                new_expression += ' '
    return new_expression.strip()

# функция для задания приоритетов операциям - для построения постфиксной нотации
def priority(operation):
    if operation == '*' or operation == '/':
        return 3
    elif operation == '+' or operation == '-':
        return 2
    elif operation == '(':
        return 1

# функция для создания постфиксной записи
def postfix_notation(expression):
    list_elements = expression.split()
    stack = []
    result = []
    for i in list_elements:
        if i.isdigit():
            result.append(int(i))
        elif i in ['+', '-', '*', '/', '(', ')']:
            if i == ')':
                while priority(stack[-1]) != 1:
                    result.append(stack.pop())
                stack.pop()
            else:
                if i == '(' or len(stack) == 0 or priority(stack[(len(stack)-1)]) < priority(i):
                    stack.append(i)
                else:
                    while len(stack) > 0 and priority(stack[len(stack)-1]) >= priority(i):
                        result.append(stack.pop())
                    stack.append(i)
    while len(stack) > 0:
        result.append(stack.pop())
    return result

#  функция для вычисления результата обратной польской записи
def calculation(opn):
    actions = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: y / x
    }

    stack = []
    for i in opn:
        if i in actions:
            num1, num2 = stack.pop(), stack.pop()
            stack.append(actions[i](num1, num2))
        else:
            stack.append(i)

    result = stack.pop()
    if result == int(result):
        result = int(result)
    return result






