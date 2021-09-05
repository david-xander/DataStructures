from datastructures.stack.stack_calc_operations_in_paterentheses.calcparentheses import *
import unittest


class TestCalc(unittest.TestCase):

    def test_adding_two_items_returns_sum(self):
        self.assertEqual(3, Calc('(1+2)').result())

    def test_sum_of_nested_parentheses(self):
        self.assertEqual(4, Calc('[1+(1+2)]').result())
        self.assertEqual(7, Calc('{[1+(1+2)]+3}').result())

    def test_diferent_operations(self):
        self.assertEqual(2, Calc('[5-(1+2)]').result())
        self.assertEqual(15, Calc('[5*(1+2)]').result())
        self.assertEqual(1, Calc('{6/[2*(1+2)]}').result())

    def test_equality_of_operations(self):
        # As Calc(input) is a value object
        self.assertEqual(Calc('{[1+(1+2)]+3}'), Calc('[4+(1+2)]'))        

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
