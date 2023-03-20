"""Модуль состоит из одной функции, описание которой ниже"""


def function(file_name, arr):
    """Функция генерирует строки,
    в которых встречается хоть одно слово в массиве arr"""
    set_words = set(map(lambda x: x.lower(), arr))
    with open(file_name, "r") as file_pointer:
        while True:
            line = file_pointer.readline()
            if not line:
                break
            tmp = set(line.lower().split())
            if tmp.intersection(set_words):
                yield line.rstrip()
