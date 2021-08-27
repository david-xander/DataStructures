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
                stack.push(char)                
            elif char in grouping_end:
                operand1 = stack.pop()
                operator = stack.pop()
                operand2 = stack.pop()
                res += int(operand1)+int(operand2)
            else:
                stack.push(char)

        return res
    

if __name__ == '__main__':
    print(BalanceParentheses().Calc('(1+2)'))
