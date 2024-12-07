"""
Функция раскладывает список любой вложенности (вложенные СПИСКИ !!!)
в плоский список.
Другие итерируемые объекты не раскладываю - такая задача не ставилась
"""


def fun_flat(lis):
    res = []
    while True:
        some_iter = False
        for i in lis:
            if i.__class__ == list:
                res.extend(i)
                some_iter = True
            else:
                res.append(i)
        lis = res
        res = []
        if not some_iter:
            break
    return lis


"""Доработать класс FlatIterator в коде
ниже. Должен получиться итератор, который
принимает список списков и возвращает их
плоское представление, т.е.последовательность, состоящую
из вложенных элементов. Функция test в коде ниже также
должна отработать без ошибок."""


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = sum(list_of_list, [])

    def __iter__(self):
        self.cur = 0
        return self

    def __next__(self):
        while True:
            if self.cur >= len(self.list_of_list):
                raise StopIteration
            item = self.list_of_list[self.cur]
            self.cur += 1
            return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    # for i in FlatIterator(list_of_lists_1):
    #     print(i)

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print("Задача 1 прошла")


if __name__ == '__main__':
    test_1()

"""Доработать функцию flat_generator. Должен получиться
генератор, который принимает список списков и возвращает
их плоское представление. Функция test в коде ниже также
должна отработать без ошибок."""
import types


def flat_generator(list_of_lists):
    list_of_list = sum(list_of_lists, [])
    i = 0
    while i < len(list_of_list):
        yield list_of_list[i]
        i += 1


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print("Задача 2 прошла")


if __name__ == '__main__':
    test_2()

"""3. * Необязательное задание.Написать итератор, аналогичный
итератору из задания 1, но обрабатывающий списки с любым уровнем
вложенности.Шаблон и тест в коде ниже:"""


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = fun_flat(list_of_list)
        # self.list_of_list = sum(self.list_of_list,[])

    def __iter__(self):
        self.cur = 0
        return self

    def __next__(self):
        while True:
            if self.cur >= len(self.list_of_list):
                raise StopIteration
            item = self.list_of_list[self.cur]
            self.cur += 1
            return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    list_of_lists_2 = fun_flat(list_of_lists_2)
    for flat_iterator_item, check_item in zip(
            (list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
    print("Задача 3 прошла")

"""4. * Необязательное задание.Написать генератор, аналогичный
генератору из задания 2, но обрабатывающий списки с любым уровнем
вложенности.Шаблон и тест в коде ниже:
"""
import types


def flat_generator(list_of_list):
    list_of_list = fun_flat(list_of_list)
    i = 0
    while i < len(list_of_list):
        yield list_of_list[i]
        i += 1


def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
    print("Задача 4 прошла")
