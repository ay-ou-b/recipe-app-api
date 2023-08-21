from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    def test_add(self):
        result = calc.add(1, 2)
        self.assertEqual(result, 3)


class Substarct(SimpleTestCase):
    def test_subtract(self):
        result = calc.subtract(1, 2)
        self.assertEqual(result, -1)