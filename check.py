# организация проверок

# функция для проверки правильности введённого выражения
"""
   я не делала слишком глубокую проверку:
        либо введено целое число для одиночных вычислений
        либо арифметическое выражение - и вот тут я проверила только, что
            - выражение начинается с цифры или с открывающей скобки
            - выражение заканчивается цифрой или закрывающей скобкой
            - соблюден баланс скобок
"""
def not_an_expression(expression):
    if not (expression[0].isdigit() or expression[0]=='('):
        return False
    if not(expression[-1].isdigit() or expression[-1]==')'):
        return False
    for i in expression:
        if not (i in '0123456789 +-*/()'):
            return False
    if expression.count('(') != expression.count(')'):
        return False
    return True

