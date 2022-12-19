"""
Выполнил Прокофьев А.А.
Фт-210008

Думаю весьма неуместно и слишком просто решать лабу при помощи print(eval(input())),
поэтому я решил лабу без использования этой функции
"""

import re # для разделения строки при помощи регулярных выражений

def run_operator(first_value:int, second_value:int, operator = "+"):
    """
    обёртка для упрощённого выполнения функции
    """

    # все возможные операторы прописаны в словаре. если будет неизвестный оператор, то будет ошибка
    expressions = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }

    return expressions[operator](first_value, second_value)


def main():
    """
    Главная функция
    """
    # ввод строки
    raw_expression = input("Введите выражение >> ")

    # очищаем пробелы, т.к. привычка писать с пробелами :)
    while raw_expression.count(" ") != 0:
        raw_expression = raw_expression.replace(" ", "")

    # разделяем строку на числа при помощи регулярного выражения
    value_list = list(map(int, re.split('[-+*/]', raw_expression)))

    if len(value_list) > 3:
        raise Exception("слишком много чисел")

    # ищем операторы которые есть в выражении (тооочно таким же образом)
    operators_list = list(filter(lambda x: x != "", re.split(r'\d+', raw_expression)))

    # print(value_list, operators_list)

    if len(operators_list) == 2:
        if operators_list[1] in ["*", "/"]:
            first_step = run_operator(value_list[1], value_list[2], operators_list[1])
            second_step = run_operator(value_list[0], first_step, operators_list[0])

        else:
            first_step = run_operator(value_list[0], value_list[1], operators_list[0])
            second_step = run_operator(value_list[2], first_step, operators_list[1])

        result = second_step

    else:
        result = run_operator(value_list[0], value_list[1], operators_list[0])

    print("Вывод", "\t"*2, "<<", result)
    return 0


if __name__ == "__main__":
    main()
