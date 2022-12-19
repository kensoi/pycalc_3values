"""
Выполнил Прокофьев А.А.
Фт-210008

Думаю весьма неуместно и слишком просто решать лабу при помощи print(eval(input())),
поэтому я решил лабу без использования этой функции
"""

import re # для разделения строки при помощи регулярных выражений
import logging # для введения log файла

logging.basicConfig(
    filename="./log.txt",
    level=logging.DEBUG, format="%(asctime)s [%(levelname)s]\t%(message)s", encoding="utf-8"
    )

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

    logging.debug(
        "Совершено вычисление при помощи выражения %s %s %s",
        first_value, operator, second_value
        )

    return expressions[operator](first_value, second_value)


def main():
    """
    Главная функция
    """
    logging.info(
        "Программа начата"
        )
    # ввод строки
    raw_expression = input("Введите выражение >> ")

    logging.debug(
        "Введено выражение : %s ", raw_expression
        )
    # очищаем пробелы, т.к. привычка писать с пробелами :)
    while raw_expression.count(" ") != 0:
        logging.debug(
            "Очистка пробелов"
            )
        raw_expression = raw_expression.replace(" ", "")
    logging.debug(
        "Очистка пробелов"
        )
    # разделяем строку на числа при помощи регулярного выражения
    value_list = list(map(int, re.split('[-+*/]', raw_expression)))

    logging.debug(
        "числа в выражении : %s ", value_list
        )
    logging.debug(
        "длина списка чисел : %s ", len(value_list)
        )
    if len(value_list) > 3:
        raise Exception("слишком много чисел")

    # ищем операторы которые есть в выражении (тооочно таким же образом)
    operators_list = list(filter(lambda x: x != "", re.split(r'\d+', raw_expression)))

    logging.debug(
        "список операторов : %s ", operators_list
        )
    # print(value_list, operators_list)

    logging.info(
        "парсинг завершён, переход к вычислениям"
        )
    if len(operators_list) == 2:
        if operators_list[1] in ["*", "/"]:
            logging.info(
                "начинаем с второго оператора по приоритету"
                )
            first_step = run_operator(value_list[1], value_list[2], operators_list[1])
            second_step = run_operator(value_list[0], first_step, operators_list[0])

        else:
            logging.info(
                "начинаем с первого оператора по приоритету"
                )
            first_step = run_operator(value_list[0], value_list[1], operators_list[0])
            second_step = run_operator(value_list[2], first_step, operators_list[1])

        result = second_step

    else:
        logging.info(
            "вычисление без приоритетов"
            )
        result = run_operator(value_list[0], value_list[1], operators_list[0])

    logging.info(
        "вывод решения в консоль"
        )
    print("Вывод", "\t"*2, "<<", result)
    return 0


if __name__ == "__main__":
    main()
