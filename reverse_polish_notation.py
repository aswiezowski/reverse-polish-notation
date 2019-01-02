
import re
from functools import reduce

class Element:

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def __repr__(self):
        return self._value

    def __eq__(self, other):
        return self.value == other.value


class NumberElement(Element):

    def __init__(self, number_value):
        Element.__init__(self, number_value)

    def numeric_value(self):
        return float(self.value)


class OperatorElement(Element):

    operators_functions = {"^": lambda x, y: x ** y,
                           "*": lambda x, y: x * y,
                           "/": lambda x, y: x / y,
                           "%": lambda x, y: x % y,
                           "+": lambda x, y: x + y,
                           "-": lambda x, y: x - y}

    def __init__(self, value):
        Element.__init__(self, value)
    
    def calculate(self, x, y):
        return self.operators_functions[self.value](x, y)


class ReversePolishNotationExpression:

    def __init__(self, rpn):
        self.rpn = rpn

    @property
    def value(self):
        return self.rpn

    def calculate(self):
        stack = []
        for element in self.rpn:
            if isinstance(element, OperatorElement):
                x = stack.pop()
                y = stack.pop()
                result = element.calculate(y,x)
                stack.append(result)
            else:
                stack.append(element.numeric_value())
        return stack.pop()

    def __repr__(self):
        return reduce(lambda x, y: str(x) + " " + str(y), self.rpn)


class AlgebraicExpressionParser:

    left_brace = "("
    operators = {"^": 3, "*": 2, "/": 2, "%": 2, "+": 1, "-": 1, left_brace: 0}
    digit_pattern = re.compile("[\\w\\.]")

    def __init__(self, algebraic_expression):
        self.algebraic_expression = algebraic_expression

    def convert_to_rpn(self):
        elements = []
        operators_stack = []
        numeric_symbol = ''
        for element in self.algebraic_expression:
            if not self.digit_pattern.match(element) and len(numeric_symbol) != 0:
                elements.append(NumberElement(numeric_symbol))
                numeric_symbol = ''
            if self.digit_pattern.match(element):
                numeric_symbol += element
            elif element == self.left_brace:
                operators_stack.append(element)
            elif element == ")":
                while operators_stack[-1] != self.left_brace:
                    elements.append(OperatorElement(operators_stack.pop()))
                operators_stack.pop()
            elif element in self.operators:
                o1 = element
                while len(operators_stack) > 0 and self.operators[o1] <= self.operators[operators_stack[-1]]:
                    elements.append(OperatorElement(operators_stack.pop()))
                operators_stack.append(o1)

        if len(numeric_symbol) != 0:
            elements.append(NumberElement(numeric_symbol))
 
        while len(operators_stack) > 0:
            operator = operators_stack.pop()
            if operator == "(":
                raise RuntimeError("Incorrect expression syntax. End brace not found")
            elements.append(OperatorElement(operator))
        
        return ReversePolishNotationExpression(elements)

if __name__ == '__main__':
    algebraic_expression = input("Enter algebraic expression: ")
    rpn_expression = AlgebraicExpressionParser(
        algebraic_expression).convert_to_rpn()
    print(rpn_expression)
