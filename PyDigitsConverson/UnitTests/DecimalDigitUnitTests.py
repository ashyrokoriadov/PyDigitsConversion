from enum import Enum
from digit import Digit, DigitType
from decimal_digit import DecimalDigit
import unittest

class Test_DecimalDigitUnitTests(unittest.TestCase):
    #def test_A(self):
        #self.fail("Not implemented")

    def test_conversion_to_binary_only_integer_part(self):
        decimal_digit = DecimalDigit()
        decimal_digit.digit_value = '12'
        binary_digit = decimal_digit.get_binary()        
        self.assertEqual(binary_digit, "1100.0", "10: 12 should be 2: 1100.0")

    def test_conversion_to_binary_integer__and_fractional_parts(self):
        decimal_digit = DecimalDigit()
        decimal_digit.digit_value = '12.18'
        binary_digit = decimal_digit.get_binary()        
        self.assertEqual(binary_digit, "1100.0010111000", "10: 12.18 should be 2: 1100.0010111000")

    def test_conversion_to_decimal_only_integer_part(self):
        decimal_digit = DecimalDigit()
        decimal_digit.digit_value = '12'
        decimal_digit_new = decimal_digit.get_decimal()        
        self.assertEqual(decimal_digit_new, "12", "10: 12 should be 10: 12")

    def test_conversion_to_decimal_integer__and_fractional_parts(self):
        decimal_digit = DecimalDigit()
        decimal_digit.digit_value = '12.18'
        decimal_digit_new = decimal_digit.get_decimal()        
        self.assertEqual(decimal_digit_new, "12.18", "10: 12.18 should be 10: 12.18")

if __name__ == '__main__':
    try:
        unittest.main()
    except Exception as e:
        print("Unexpected error:", inst.args)
