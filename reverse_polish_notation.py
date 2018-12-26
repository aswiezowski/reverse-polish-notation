
import re

class Element:

    def __init__(self):
        self.value = ''

class NumberElement(Element):

    def __init__(self):
            Element.__init__(self)

class OpertatorElement(Element):

    def __init__(self):
            Element.__init__(self)

class ReversePolishNotation:

    operators = {"^": 3, "*": 2, "/": 2, "%": 2, "+": 1, "-": 1, "(": 0}
    digit_pattern = re.compile("\\w")

    def convert_to_rpn(self, algebraic_expression):
        output = ""
        operators_stack = []
        for element in algebraic_expression:
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
        return output

algebraic_expression = input("Enter algebraic expression: ")
print(ReversePolishNotation().convert_to_rpn(algebraic_expression))
