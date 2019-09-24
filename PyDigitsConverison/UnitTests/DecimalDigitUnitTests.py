from enum import Enum
from digit import Digit, DigitType
from decimal_digit import DecimalDigit
import unittest

class Test_DecimalDigitUnitTests(unittest.TestCase):

    def setUp(self):
        self.decimal_digit = DecimalDigit()

    def test_conversion_to_binary_only_integer_part(self):
        self.decimal_digit.digit_value = '12'
        binary_digit = self.decimal_digit.get_binary()        
        self.assertEqual(binary_digit, "1100.0", "10: 12 should be 2: 1100.0")

    def test_conversion_to_binary_integer__and_fractional_parts(self):
        self.decimal_digit.digit_value = '12.18'
        binary_digit = self.decimal_digit.get_binary()        
        self.assertEqual(binary_digit, "1100.0010111000", "10: 12.18 should be 2: 1100.0010111000")

    def test_conversion_to_decimal_only_integer_part(self):
        self.decimal_digit.digit_value = '12'
        decimal_digit_new = self.decimal_digit.get_decimal()        
        self.assertEqual(decimal_digit_new, "12", "10: 12 should be 10: 12")

    def test_conversion_to_decimal_integer__and_fractional_parts(self):
        self.decimal_digit.digit_value = '12.18'
        decimal_digit_new = self.decimal_digit.get_decimal()        
        self.assertEqual(decimal_digit_new, "12.18", "10: 12.18 should be 10: 12.18")

    def test_conversion_to_octal_only_integer_part(self):
        self.decimal_digit.digit_value = '1234'
        octal_digit = self.decimal_digit.get_octal()        
        self.assertEqual(octal_digit, "2322.0", "10: 1234 should be 8: 2322.0")

    def test_conversion_to_octal_integer__and_fractional_parts(self):
        self.decimal_digit.digit_value = '1234.56'
        octal_digit = self.decimal_digit.get_octal()        
        self.assertEqual(octal_digit, "2322.4365605075", "10: 1234.56 should be 8: 2322.4365605075")

    def test_conversion_to_hexadecimal_only_integer_part(self):
        self.decimal_digit.digit_value = '1234'
        hexadecimal_digit = self.decimal_digit.get_hexadecimal()        
        self.assertEqual(hexadecimal_digit, "4D2.0", "10: 1234 should be 8: 4D2")

    def test_conversion_to_hexadecimal_integer__and_fractional_parts(self):
        self.decimal_digit.digit_value = '1234.56'
        hexadecimal_digit = self.decimal_digit.get_hexadecimal()        
        self.assertEqual(hexadecimal_digit, "4D2.8F5C28F5C2", "10: 1234.56 should be 16: 4D2.8F5C28F5C2")

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass

