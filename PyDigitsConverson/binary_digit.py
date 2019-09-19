import math 
from digit import Digit, DigitType

class BinaryDigit(Digit):
    """description of class"""

    def __init__(self, digit_value='0', digit_type=2, separator='.'):
        super().__init__(digit_value=digit_value, digit_type=digit_type, separator=separator) 
        self.separator = separator
        self.digit_type = digit_type
        self.digit_value = digit_value

    def get_decimal(self):
        return self._get_decimal_integer() +self.separator + self._get_decimal_fraction()

    def get_binary(self):
        return self.digit_value

    def get_octal(self):
        return self._get_value(8)

    def get_hexadecimal(self):
        return self._get_value(16)

    def _get_decimal_integer(self):
        sum = 0
        i = 0

        value = self.digit_value.replace(self.separator, Digit._default_separator)
        value = str(math.trunc(float(value)))

        length = len(value)
        for item in value:
            sum += int(item) * (2 ** (length - i - 1))
            i +=1
        return  str(sum)

    def _get_decimal_fraction(self):
        sum = 0
        i = 0

        value = self.digit_value.replace(self.separator, Digit._default_separator)
        separator_position = value.find(Digit._default_separator)
        value = value[separator_position+1:]

        length = len(value)
        for item in value:
            sum += int(item) * (2 ** -(i + 1))
            i +=1
        return  str(sum)[2:]


