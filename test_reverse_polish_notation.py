import unittest

from reverse_polish_notation import AlgebraicExpressionParser, NumberElement, OperatorElement


class AlgebraicExpressionParserCase(unittest.TestCase):

    def test_adding_two_symbols(self):
        rpn = AlgebraicExpressionParser("a+b").convert_to_rpn()
        self.assertEqual(rpn.value, [NumberElement("a"), NumberElement("b"), OperatorElement("+")])

    def test_add_subtract_three_symbols(self):
        rpn = AlgebraicExpressionParser("a+b-c").convert_to_rpn()
        self.assertEqual(rpn.value, [NumberElement("a"), NumberElement("b"), OperatorElement("+"), NumberElement("c"), OperatorElement("-")])

    def test_add_multiply_three_symbols(self):
        rpn = AlgebraicExpressionParser("a+b*c").convert_to_rpn()
        self.assertEqual(rpn.value, [NumberElement("a"), NumberElement(
            "b"), NumberElement("c"), OperatorElement("*"), OperatorElement("+")])

    def test_add_multiply_paranthesis_three_symbols(self):
        rpn = AlgebraicExpressionParser("(a+b)*c").convert_to_rpn()
        self.assertEqual(rpn.value, [NumberElement("a"), NumberElement("b"), OperatorElement("+"), 
        NumberElement("c"), OperatorElement("*")])

    def test_complex_expression(self):
        rpn = AlgebraicExpressionParser("12 + a * (b * c + d / e)").convert_to_rpn()
        self.assertEqual(rpn.value, [NumberElement("12"), NumberElement("a"), NumberElement("b"), NumberElement("c"), OperatorElement("*"), 
        NumberElement("d"), NumberElement("e"), OperatorElement("/"), OperatorElement("+"), OperatorElement("*"), OperatorElement("+")])

    def test_parsing_floats(self):
        rpn = AlgebraicExpressionParser("23.456-78.09").convert_to_rpn()
        self.assertEqual(rpn.value, [NumberElement("23.456"), NumberElement("78.09"), OperatorElement("-")])
    def test_calculate_adding(self):
        rpn = AlgebraicExpressionParser("2.1+1.9").convert_to_rpn()
        self.assertEqual(rpn.calculate(), 4)

    def test_calculate_priority(self):
        rpn = AlgebraicExpressionParser("2-5%4+4*(5-1)/2^3").convert_to_rpn()
        self.assertEqual(rpn.calculate(), 3)
