from enum import Enum
from digit import Digit, DigitType
from decimal_digit import DecimalDigit
from octal_digit import OctalDigit
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

class Test_OctalDigitUnitTests(unittest.TestCase):

    def setUp(self):
        self.decimal_digit_integer = OctalDigit()
        self.decimal_digit_integer.digit_value='12475.0'
        self.decimal_digit_integer_and_fraction = OctalDigit()
        self.decimal_digit_integer_and_fraction.digit_value='12475.30712601014'

    def test_conversion_to_binary_only_integer_part(self):
        binary_digit = self.decimal_digit_integer.get_binary()        
        self.assertEqual(binary_digit, "1010100111101.0", "8: 12475 should be 2: 1010100111101.0")

    def test_conversion_to_binary_integer__and_fractional_parts(self):
        binary_digit = self.decimal_digit_integer_and_fraction.get_binary()        
        self.assertEqual(binary_digit, "1010100111101.0110001110", "8: 12475.30712601014 should be 2: 1010100111101.0110001110")

    def test_conversion_to_decimal_only_integer_part(self):
        decimal_digit_new = self.decimal_digit_integer.get_decimal()       
        self.assertEqual(decimal_digit_new, "5437.0", "8: 12475 should be 10: 5437.0")

    def test_conversion_to_decimal_integer__and_fractional_parts(self):
        decimal_digit_new = self.decimal_digit_integer_and_fraction.get_decimal()        
        self.assertEqual(decimal_digit_new, "5437.3889999999664724", "8: 12475.30712601014 should be 10: 5437.3889999999664724")

    def test_conversion_to_octal_only_integer_part(self):
        octal_digit = self.decimal_digit_integer.get_octal()        
        self.assertEqual(octal_digit, "12475.0", "8: 12475 should be 8: 12475.0")

    def test_conversion_to_octal_integer__and_fractional_parts(self):
        octal_digit = self.decimal_digit_integer_and_fraction.get_octal()        
        self.assertEqual(octal_digit, "12475.30712601014", "8: 12475.30712601014 should be 8: 12475.30712601014")

    def test_conversion_to_hexadecimal_only_integer_part(self):
        hexadecimal_digit = self.decimal_digit_integer.get_hexadecimal()        
        self.assertEqual(hexadecimal_digit, "153D.0", "8: 12475 should be 8: 153D")

    def test_conversion_to_hexadecimal_integer__and_fractional_parts(self):
        hexadecimal_digit = self.decimal_digit_integer_and_fraction.get_hexadecimal()        
        self.assertEqual(hexadecimal_digit, "153D.6395810624", "8: 12475.30712601014 should be 16: 153D.6395810624")

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass

