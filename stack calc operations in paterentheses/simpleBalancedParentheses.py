from datastructures import Stack
import re

class BalanceParentheses:

    def Calc(self, input):
        res = 0
        stack = Stack()
        stack_parentheses = Stack()
        grouping_start=['{','[','(']
        grouping_end=['}',']',')']
        for char in input:
            if char in grouping_start:
                stack_parentheses.push(char)
            elif char in grouping_end:
                actual = grouping_start[grouping_end.index(char)]
                previous = stack_parentheses.pop()
                if actual == previous:
                    operand1 = stack.pop()
                    operator = stack.pop()
                    operand2 = stack.pop()
                    res = int(operand1)+int(operand2)
                    stack.push(str(res))
                else:
                    raise ValueError('Invalid input')
            else:
                stack.push(char)

        return res
    

if __name__ == '__main__':
    print(BalanceParentheses().Calc('[1+(1+2)]'))
