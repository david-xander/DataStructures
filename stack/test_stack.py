from simpleBalancedParentheses import BalanceParentheses
import unittest


class TestBalanceParentheses(unittest.TestCase):

    def test_adding_two_items_returns_sum(self):
        self.assertEqual(3, BalanceParentheses().Calc('(1+2)'))

    def test_sum_of_nested_parentheses(self):
        self.assertEqual(4, BalanceParentheses().Calc('[1+(1+2)]'))

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
