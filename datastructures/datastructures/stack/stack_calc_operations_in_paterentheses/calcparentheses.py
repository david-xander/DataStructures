from datastructures.stack.stack_calc_operations_in_paterentheses.datastructures import Stack
import re

class Calc:
    def __init__(self, input) -> None:
        self.input = input

    def __eq__(self, o: object) -> bool:
        return self.result() == o.result()

    def result(self) -> int:
        input = self.input
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
                    operand2 = stack.pop()
                    operator = stack.pop()
                    operand1 = stack.pop()
                    res = self.operate(operand1, operand2, operator)
                    stack.push(str(res))
                else:
                    raise ValueError('Invalid input')
            else:
                stack.push(char)

        return res
    
    def operate(self, operand1, operand2, operator):
        res = 0
        if operator == '+':
            res = int(operand1)+int(operand2)
        elif operator == '-':
            res = int(operand1)-int(operand2)
        elif operator == '*':
            res = int(operand1)*int(operand2)
        elif operator == '/':
            res = int(operand1)//int(operand2)                        
        return res

if __name__ == '__main__':
    print(Calc('{30/[5*(1+2)]}').result())
