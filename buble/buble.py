import unittest


def bubble_sort(array: list[float]) -> list[float]:
    """Сортировка списка методом пузырька по возрастанию."""
    length = len(array)
    for bypass in range(1, length):
        for k in range(length - bypass):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
    return array


class TestBubbleSort(unittest.TestCase):
    """Тестируем функцию bubble_sort."""

    def test_int_float(self):
        # С несортированным списком чисел
        call = bubble_sort([1, 2, 3.5, 1.5, 2.7, 1.6])
        result = [1, 1.5, 1.6, 2, 2.7, 3.5]
        self.assertEqual(
            call, result, 'Функция bubble_sort некорректно работает со списком чисел'
        )

    def test_empty(self):
        # С пустым списком
        call = bubble_sort([])
        result = []
        self.assertEqual(
            call, result, 'Функция bubble_sort некорректно работает с пустым списком'
        )
