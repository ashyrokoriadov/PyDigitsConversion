from enum import Enum
from digit import Digit, DigitType
from decimal_digit import DecimalDigit
from octal_digit import OctalDigit
from binary_digit import BinaryDigit
from hexadecimal_digit import HexadecimalDigit
import unittest

class Test_DecimalDigit(unittest.TestCase):

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

    def test_passed_value_is_null_hexadecimal(self):
        self.decimal_digit.digit_value = None
        with self.assertRaises(ValueError) as cm: 
            self.decimal_digit.get_hexadecimal() 
    
    def test_passed_value_is_null_binary(self):
        self.decimal_digit.digit_value = None
        with self.assertRaises(ValueError) as cm: 
            self.decimal_digit.get_binary() 

    def test_passed_value_is_null_decimal(self):
        self.decimal_digit.digit_value = None
        with self.assertRaises(ValueError) as cm: 
            self.decimal_digit.get_decimal() 

    def test_passed_value_is_null_octal(self):
        self.decimal_digit.digit_value = None
        with self.assertRaises(ValueError) as cm:    
            self.decimal_digit.get_octal()
    
    def test_passed_value_is_empty_hexadecimal(self):
        self.decimal_digit.digit_value = ''
        with self.assertRaises(ValueError) as cm: 
            self.decimal_digit.get_hexadecimal() 
    
    def test_passed_value_is_empty_binary(self):
        self.decimal_digit.digit_value = ''
        with self.assertRaises(ValueError) as cm: 
            self.decimal_digit.get_binary() 

    def test_passed_value_is_empty_decimal(self):
        self.decimal_digit.digit_value = ''
        with self.assertRaises(ValueError) as cm: 
            self.decimal_digit.get_decimal() 

    def test_passed_value_is_empty_octal(self):
        self.decimal_digit.digit_value = ''
        with self.assertRaises(ValueError) as cm:    
            self.decimal_digit.get_octal() 

    def test_passed_value_is_nan_hexadecimal(self):
        self.decimal_digit.digit_value = 'ABC'
        with self.assertRaises(ValueError) as cm: 
            self.decimal_digit.get_hexadecimal() 
    
    def test_passed_value_is_nan_binary(self):
        self.decimal_digit.digit_value = 'ABC'
        with self.assertRaises(ValueError) as cm: 
            self.decimal_digit.get_binary() 

    def test_passed_value_is_nan_decimal(self):
        self.decimal_digit.digit_value = 'ABC'
        with self.assertRaises(ValueError) as cm: 
            self.decimal_digit.get_decimal() 

    def test_passed_value_is_nan_octal(self):
        self.decimal_digit.digit_value = 'ABC'
        with self.assertRaises(ValueError) as cm:    
            self.decimal_digit.get_octal() 

    def test_passed_value_is_whitespace_hexadecimal(self):
        self.decimal_digit.digit_value = '  '
        with self.assertRaises(ValueError) as cm: 
            self.decimal_digit.get_hexadecimal() 
    
    def test_passed_value_is_whitespace_binary(self):
        self.decimal_digit.digit_value = '   '
        with self.assertRaises(ValueError) as cm: 
            self.decimal_digit.get_binary() 

    def test_passed_value_is_whitespace_decimal(self):
        self.decimal_digit.digit_value = '   '
        with self.assertRaises(ValueError) as cm: 
            self.decimal_digit.get_decimal() 

    def test_passed_value_is_whitespace_octal(self):
        self.decimal_digit.digit_value = '   '
        with self.assertRaises(ValueError) as cm:    
            self.decimal_digit.get_octal() 

class Test_BinaryDigit(unittest.TestCase):

    def setUp(self):
        self.binary_digit_integer = BinaryDigit()
        self.binary_digit_integer.digit_value = '111010011'
        self.binary_digit_integer_and_fraction = BinaryDigit()
        self.binary_digit_integer_and_fraction.digit_value = '111010011.11100011110'

    def test_conversion_to_binary_only_integer_part(self):
        binary_digit = self.binary_digit_integer.get_binary()        
        self.assertEqual(binary_digit, "111010011", "2: 111010011 should be 2: 111010011")

    def test_conversion_to_binary_integer__and_fractional_parts(self):
        binary_digit = self.binary_digit_integer_and_fraction.get_binary()        
        self.assertEqual(binary_digit, "111010011.11100011110", "2: 111010011.11100011110 should be 2: 111010011.11100011110")

    def test_conversion_to_decimal_only_integer_part(self):
        decimal_digit = self.binary_digit_integer.get_decimal()        
        self.assertEqual(decimal_digit, "467.0", "2: 111010011.0 should be 10: 467.0")

    def test_conversion_to_decimal_integer__and_fractional_parts(self):
        decimal_digit_new = self.binary_digit_integer_and_fraction.get_decimal()        
        self.assertEqual(decimal_digit_new, "467.8896484375", "2: 111010011.11100011110 should be 10: 467.8896484375")

    def test_conversion_to_octal_only_integer_part(self):
        octal_digit = self.binary_digit_integer.get_octal()        
        self.assertEqual(octal_digit, "723.0", "2: 111010011 should be 8: 723.0")

    def test_conversion_to_octal_integer__and_fractional_parts(self):
        octal_digit = self.binary_digit_integer_and_fraction.get_octal()        
        self.assertEqual(octal_digit, "723.7074", "2: 111010011.11100011110 should be 8: 723.7074")

    def test_conversion_to_hexadecimal_only_integer_part(self):
        hexadecimal_digit = self.binary_digit_integer.get_hexadecimal()        
        self.assertEqual(hexadecimal_digit, "1D3.0", "2: 111010011 should be 8: 1D3.0")

    def test_conversion_to_hexadecimal_integer__and_fractional_parts(self):
        hexadecimal_digit = self.binary_digit_integer_and_fraction.get_hexadecimal()        
        self.assertEqual(hexadecimal_digit, "1D3.E3C", "2: 111010011.11100011110 should be 16: 1D3.E3C")

    def test_passed_value_is_null_hexadecimal(self):
        self.binary_digit_integer.digit_value = None
        with self.assertRaises(ValueError) as cm: 
            self.binary_digit_integer.get_hexadecimal() 
    
    def test_passed_value_is_null_binary(self):
        self.binary_digit_integer.digit_value = None
        with self.assertRaises(ValueError) as cm: 
            self.binary_digit_integer.get_binary() 

    def test_passed_value_is_null_decimal(self):
        self.binary_digit_integer.digit_value = None
        with self.assertRaises(ValueError) as cm: 
            self.binary_digit_integer.get_decimal() 

    def test_passed_value_is_null_octal(self):
        self.binary_digit_integer.digit_value = None
        with self.assertRaises(ValueError) as cm:    
            self.binary_digit_integer.get_octal()
    
    def test_passed_value_is_empty_hexadecimal(self):
        self.binary_digit_integer.digit_value = ''
        with self.assertRaises(ValueError) as cm: 
            self.binary_digit_integer.get_hexadecimal() 
    
    def test_passed_value_is_empty_binary(self):
        self.binary_digit_integer.digit_value = ''
        with self.assertRaises(ValueError) as cm: 
            self.binary_digit_integer.get_binary() 

    def test_passed_value_is_empty_decimal(self):
        self.binary_digit_integer.digit_value = ''
        with self.assertRaises(ValueError) as cm: 
            self.binary_digit_integer.get_decimal() 

    def test_passed_value_is_empty_octal(self):
        self.binary_digit_integer.digit_value = ''
        with self.assertRaises(ValueError) as cm:    
            self.binary_digit_integer.get_octal() 

    def test_passed_value_is_nan_hexadecimal(self):
        self.binary_digit_integer.digit_value = 'ABC'
        with self.assertRaises(ValueError) as cm: 
            self.binary_digit_integer.get_hexadecimal() 
    
    def test_passed_value_is_nan_binary(self):
        self.binary_digit_integer.digit_value = 'ABC'
        with self.assertRaises(ValueError) as cm: 
            self.binary_digit_integer.get_binary() 

    def test_passed_value_is_nan_decimal(self):
        self.binary_digit_integer.digit_value = 'ABC'
        with self.assertRaises(ValueError) as cm: 
            self.binary_digit_integer.get_decimal() 

    def test_passed_value_is_nan_octal(self):
        self.binary_digit_integer.digit_value = 'ABC'
        with self.assertRaises(ValueError) as cm:    
            self.binary_digit_integer.get_octal() 

    def test_passed_value_is_whitespace_hexadecimal(self):
        self.binary_digit_integer.digit_value = '  '
        with self.assertRaises(ValueError) as cm: 
            self.binary_digit_integer.get_hexadecimal() 
    
    def test_passed_value_is_whitespace_binary(self):
        self.binary_digit_integer.digit_value = '   '
        with self.assertRaises(ValueError) as cm: 
            self.binary_digit_integer.get_binary() 

    def test_passed_value_is_whitespace_decimal(self):
        self.binary_digit_integer.digit_value = '   '
        with self.assertRaises(ValueError) as cm: 
            self.binary_digit_integer.get_decimal() 

    def test_passed_value_is_whitespace_octal(self):
        self.binary_digit_integer.digit_value = '   '
        with self.assertRaises(ValueError) as cm:    
            self.binary_digit_integer.get_octal() 

class Test_OctalDigit(unittest.TestCase):

    def setUp(self):
        self.digit_integer = OctalDigit()
        self.digit_integer.digit_value='12475.0'
        self.digit_integer_and_fraction = OctalDigit()
        self.digit_integer_and_fraction.digit_value='12475.30712601014'

    def test_conversion_to_binary_only_integer_part(self):
        binary_digit = self.digit_integer.get_binary()        
        self.assertEqual(binary_digit, "1010100111101.0", "8: 12475 should be 2: 1010100111101.0")

    def test_conversion_to_binary_integer__and_fractional_parts(self):
        binary_digit = self.digit_integer_and_fraction.get_binary()        
        self.assertEqual(binary_digit, "1010100111101.0110001110", "8: 12475.30712601014 should be 2: 1010100111101.0110001110")

    def test_conversion_to_decimal_only_integer_part(self):
        decimal_digit_new = self.digit_integer.get_decimal()       
        self.assertEqual(decimal_digit_new, "5437.0", "8: 12475 should be 10: 5437.0")

    def test_conversion_to_decimal_integer__and_fractional_parts(self):
        decimal_digit_new = self.digit_integer_and_fraction.get_decimal()        
        self.assertEqual(decimal_digit_new, "5437.3889999999664724", "8: 12475.30712601014 should be 10: 5437.3889999999664724")

    def test_conversion_to_octal_only_integer_part(self):
        octal_digit = self.digit_integer.get_octal()        
        self.assertEqual(octal_digit, "12475.0", "8: 12475 should be 8: 12475.0")

    def test_conversion_to_octal_integer__and_fractional_parts(self):
        octal_digit = self.digit_integer_and_fraction.get_octal()        
        self.assertEqual(octal_digit, "12475.30712601014", "8: 12475.30712601014 should be 8: 12475.30712601014")

    def test_conversion_to_hexadecimal_only_integer_part(self):
        hexadecimal_digit = self.digit_integer.get_hexadecimal()        
        self.assertEqual(hexadecimal_digit, "153D.0", "8: 12475 should be 8: 153D")

    def test_conversion_to_hexadecimal_integer__and_fractional_parts(self):
        hexadecimal_digit = self.digit_integer_and_fraction.get_hexadecimal()        
        self.assertEqual(hexadecimal_digit, "153D.6395810624", "8: 12475.30712601014 should be 16: 153D.6395810624")

class Test_HexadecimalDigit(unittest.TestCase):

    def setUp(self):
        self.decimal_digit_integer = HexadecimalDigit()
        self.decimal_digit_integer.digit_value='271.0'
        self.digit_integer_and_fraction = HexadecimalDigit()
        self.digit_integer_and_fraction.digit_value='271.1C28'

    def test_conversion_to_binary_only_integer_part(self):
        binary_digit = self.decimal_digit_integer.get_binary()        
        self.assertEqual(binary_digit, "1001110001.0", "16: 271.0 should be 2: 1001110001.0")

    def test_conversion_to_binary_integer__and_fractional_parts(self):
        binary_digit = self.digit_integer_and_fraction.get_binary()        
        self.assertEqual(binary_digit, "1001110001.0001110000", "16: 271.1C28 should be 2: 1001110001.0001110000")

    def test_conversion_to_decimal_only_integer_part(self):
        decimal_digit_new = self.decimal_digit_integer.get_decimal()       
        self.assertEqual(decimal_digit_new, "625.0", "16: 271.0 should be 10: 625.0")

    def test_conversion_to_decimal_integer__and_fractional_parts(self):
        decimal_digit_new = self.digit_integer_and_fraction.get_decimal()        
        self.assertEqual(decimal_digit_new, "625.1099853515625", "16: 271.1C28 should be 10: 625.1099853515625")

    def test_conversion_to_octal_only_integer_part(self):
        octal_digit = self.decimal_digit_integer.get_octal()        
        self.assertEqual(octal_digit, "1161.0", "16: 271.0 should be 8: 1161.0")

    def test_conversion_to_octal_integer__and_fractional_parts(self):
        octal_digit = self.digit_integer_and_fraction.get_octal()        
        self.assertEqual(octal_digit, "1161.0702436560", "16: 271.1C28 should be 8: 1161.0702436560")

    def test_conversion_to_hexadecimal_only_integer_part(self):
        hexadecimal_digit = self.decimal_digit_integer.get_hexadecimal()        
        self.assertEqual(hexadecimal_digit, "271.0", "16: 271.0 should be 8: 271.0")

    def test_conversion_to_hexadecimal_integer__and_fractional_parts(self):
        hexadecimal_digit = self.digit_integer_and_fraction.get_hexadecimal()        
        self.assertEqual(hexadecimal_digit, "271.1C28", "16: 271.1C28 should be 16: 271.1C28")

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass

