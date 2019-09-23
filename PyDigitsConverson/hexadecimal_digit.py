import math 
from digit import Digit, DigitType
from decimal_digit import DecimalDigit

class HexadecimalDigit(Digit):
    """description of class"""
    def __init__(self, digit_value='0', digit_type=16, separator='.'):
        super().__init__(digit_value=digit_value, digit_type=digit_type, separator=separator) 
        self.separator = separator
        self.digit_type = digit_type
        self.digit_value = digit_value

    def get_decimal(self):
        return self._get_decimal_integer(16) + self.separator + self._get_decimal_fraction(16)

    def get_binary(self):
        decimal = self.get_decimal()
        decimal_digit = DecimalDigit(digit_value=decimal, digit_type=10, separator=self.separator)
        return decimal_digit.get_binary()

    def get_octal(self):
        decimal = self.get_decimal()
        decimal_digit = DecimalDigit(digit_value=decimal, digit_type=10, separator=self.separator)
        return decimal_digit.get_octal()

    def get_hexadecimal(self):
        return self.digit_value
       


