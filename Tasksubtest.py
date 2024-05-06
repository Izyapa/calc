import unittest


def bartender(order):
    if isinstance(order, int) and order > 0:
        return order
    return 'Извините, я не могу вас обслужить!'

ANSWER = 'Извините, я не могу вас обслужить!'

class TestBar(unittest.TestCase):

    def test_bartender(self):
        values_results = (
            (5, 5),
            (0, ANSWER),
            (0.33, ANSWER),
            (-1.999999, ANSWER),
            ("фываолдж", ANSWER),
        )
        for item in values_results:
            value, expected_result = item
            with self.subTest(value=value,
                              expected_result=expected_result,
                              msg=f'Заказ {value} фуфло',
                              ):
                result = bartender(value)
                self.assertEqual(result, expected_result)