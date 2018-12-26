
import re

class Element:

    def __init__(self, value):
        self._value = value
    
    @property
    def number_value(self):
        return self._value

class NumberElement(Element):

    def __init__(self, number_value):
        Element.__init__(self,number_value)

class OpertatorElement(Element):

    def __init__(self, value):
        Element.__init__(self, value)

class ReversePolishNotationExpression:

    def __init__(self, rpn):
        self.rpn = rpn
    
    def print(self):
        print(self.rpn)

class AlgebraicExpressionParser:

    operators = {"^": 3, "*": 2, "/": 2, "%": 2, "+": 1, "-": 1, "(": 0}
    digit_pattern = re.compile("\\w")

    def __init__(self, algebraic_expression):
        self.algebraic_expression = algebraic_expression

    def convert_to_rpn(self):
        output = ""
        operators_stack = []
        for element in self.algebraic_expression:
            if self.digit_pattern.match(element):
                output += element
            elif element == "(":
                operators_stack.append(element)
            elif element == ")":
                while operators_stack[-1] != "(":
                    output += " "+operators_stack.pop()
                operators_stack.pop()
            elif element in self.operators:
                o1 = element
                while len(operators_stack) > 0 and self.operators[o1] <= self.operators[operators_stack[-1]]:
                    output += " "+operators_stack.pop()
                operators_stack.append(o1)
            else:
                output += " "

        while len(operators_stack) > 0:
            operator = operators_stack.pop()
            if operator == "(":
                print("Incorrect expression syntax. End brace not found")
            output += " "+operator
        return ReversePolishNotationExpression(output)

algebraic_expression = input("Enter algebraic expression: ")
rpn_expression = AlgebraicExpressionParser(algebraic_expression).convert_to_rpn()
rpn_expression.print()
