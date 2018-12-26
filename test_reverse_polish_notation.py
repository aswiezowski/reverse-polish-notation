import unittest

from reverse_polish_notation import AlgebraicExpressionParser, NumberElement, OpertatorElement


class AlgebraicExpressionParserCase(unittest.TestCase):

    def test_adding_two_symbols(self):
        rpn = AlgebraicExpressionParser("a+b").convert_to_rpn()
        self.assertEqual(rpn.value, [NumberElement("a"), NumberElement("b"), OpertatorElement("+")])

    def test_add_subtract_three_symbols(self):
        rpn = AlgebraicExpressionParser("a+b-c").convert_to_rpn()
        self.assertEqual(rpn.value, [NumberElement("a"), NumberElement("b"), OpertatorElement("+"), NumberElement("c"), OpertatorElement("-")])

    def test_add_multiply_three_symbols(self):
        rpn = AlgebraicExpressionParser("a+b*c").convert_to_rpn()
        self.assertEqual(rpn.value, [NumberElement("a"), NumberElement(
            "b"), NumberElement("c"), OpertatorElement("*"), OpertatorElement("+")])

    def test_add_multiply_paranthesis_three_symbols(self):
        rpn = AlgebraicExpressionParser("(a+b)*c").convert_to_rpn()
        self.assertEqual(rpn.value, [NumberElement("a"), NumberElement("b"), OpertatorElement("+"), 
        NumberElement("c"), OpertatorElement("*")])

    def test_complex_expression(self):
        rpn = AlgebraicExpressionParser("12 + a * (b * c + d / e)").convert_to_rpn()
        self.assertEqual(rpn.value, [NumberElement("12"), NumberElement("a"), NumberElement("b"), NumberElement("c"), OpertatorElement("*"), 
        NumberElement("d"), NumberElement("e"), OpertatorElement("/"), OpertatorElement("+"), OpertatorElement("*"), OpertatorElement("+")])
