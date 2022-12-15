import OPN
import view
import model
import check

# функция для первоначального ввода: до первого корректного ввода числа или выражения
# возвращает тип работы: 1 - одиночные операнды, 2 - арифметическое выражение (с учётом скобок и приоритетов)
def input_first():
    first_launch = view.input_expression().strip()
    while not(check.not_an_expression(first_launch)):
        view.invalid_expression()
        first_launch = view.input_expression()
    if first_launch.isdigit():
        model.set_first(int(first_launch))
        return 1
    else:
        model.set_formula(first_launch)
        return 2

# функция для ввода операнда для одиночного вычисления
def input_second():
    while True:
        number = view.input_number()
        if model.get_operation() == '/' and number == 0:
            view.division_by_zero()
        else:
            model.set_second(number)
            break

# функция для ввода арифметической операции для одиночного вычисления
def input_operation():
    op = view.input_operation()
    model.set_operation(op)

# функция для организации одиночного вычисления с выводом результатов на экран
def solution():
    op = model.get_operation()
    if op == '+':
        model.addition()
    elif op == '-':
        model.subtraction()
    elif op == '/':
       model.division()
    elif op == '*':
        model.multiplication()

    result = model.get_result()
    result_str = f'{model.get_first()} {model.get_operation()} {model.get_second()} = {model.get_result()}'
    view.print_to_console(result_str)
    model.set_first(model.get_result())

# функция для реализации вычисления
# в зависимости от типа работы (одиночные вычисления или выражение) - управление передаётся
# методу solution или вычислениям по постфиксной нотации
def start():
    method = input_first()
    if method == 1:
        while True:
            input_operation()
            if model.get_operation() == '=':
                view.log_off()
                break
            input_second()
            solution()
    elif method == 2:
        expression = OPN.expression_members(model.get_formula())
        model.set_formula(expression)
        model.calc()
        output_str = f'{model.get_formula()} = {model.get_result()}'
        view.print_to_console(output_str)
        view.log_off()

