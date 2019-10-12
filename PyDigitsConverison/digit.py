from enum import Enum
import math 
import re

class Digit:
    """description of class"""

    _default_separator = '.'
    _invalid_triad = "Invalid triad."
    _invalid_tetrad = "Invalid tetrad."
    _invalid_input_string = "Invalid input string: 1. input string is null or empty; 2. invalid separator."
    _separator_missmatch = "Input string and separator missmatch."
    _validation_error = 'Value to be converted is None, empty, NaN or whitespace.'

    def __init__(self, digit_value='0', digit_type=10, separator='.'):
        self.separator = separator
        self.digit_type = digit_type
        self.digit_value = digit_value

    def get_decimal(self):
        return self.digit_value

    def get_number_for_letter(self, letter):
        switcher = {
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15,
        }
        return switcher.get(letter, -99)

    def get_letter_for_number(self, number):
        switcher = {
            10 : 'A',
            11 : 'B',
            12 : 'C',
            13 : 'D',
            14 : 'E',
            15 : 'F',
        }
        return switcher.get(number, 'Z')

    def convert_list_to_string_integer(self, list):

        result_value = ''
        for item in list:
            result_value = result_value + str(item) 

        return result_value

    def convert_list_to_string_fraction(self, list):

        result_value = ''
        counter = 0

        for item in list:

            if(counter == 10):
                break

            result_value = result_value + str(item) 
            counter += 1

        return result_value

    def _get_octal_for_triad(self, triad):
        switcher = {
                "000" : '0',
                "001" : '1',
                "010" : '2',
                "011" : '3',
                "100" : '4',
                "101" : '5',
                "110" : '6',
                "111" : '7'
            }
        return switcher.get(triad, '222')

    def _get_hexadecimal_for_tetrad(self, tetrad):
        switcher = {
                "0000" : '0',
                "0001" : '1',
                "0010" : '2',
                "0011" : '3',
                "0100" : '4',
                "0101" : '5',
                "0110" : '6',
                "0111" : '7',
                "1000" : '8',
                "1001" : '9',
                "1010" : 'A',
                "1011" : 'B',
                "1100" : 'C',
                "1101" : 'D',
                "1110" : 'E',
                "1111" : 'F'
            }
        return switcher.get(tetrad, 'ZZZZ')

    def _get_decimal_integer(self, digit_type):
        sum = 0
        i = 0

        if self.separator in self.digit_value:
            integer, fraction = self.digit_value.split(self.separator)
        else:
            integer = self.digit_value
            fraction = '0'

        value = integer

        length = len(value)
        for item in value:
            if item.isdigit():
                sum += int(item) * (digit_type ** (length - i - 1))
            else:
                item = self.get_number_for_letter(item)
                sum += int(item) * (digit_type ** (length - i - 1))
            i +=1
        return  str(sum)

    def _get_decimal_fraction(self, digit_type):
        sum = 0
        i = 0

        value = self.digit_value.replace(self.separator, Digit._default_separator)
        separator_position = value.find(Digit._default_separator)

        if separator_position == -1:
            return "0"

        value = value[separator_position+1:]

        length = len(value)
        for item in value:
            if item.isdigit():
                sum += int(item) * (digit_type ** -(i + 1))
            else:
                item = self.get_number_for_letter(item)
                sum += int(item) * (digit_type ** -(length - i - 1))
            i +=1

        sum = str(sum)
        separator_position = sum.find(Digit._default_separator)
        if separator_position == -1:
            return "0"
        return str(sum)[separator_position+1:]

    def _is_none(self):
        return self.digit_value is None

    def _is_empty_string(self):
        return self.digit_value == ''

    def _is_float_number(self):
        try:
           val = float(self.digit_value)
           return True 
        except ValueError:
           return False

    def _is_hexadecimal(self):
        pattern = re.compile("^[A-Fa-f0-9\.]+$")
        return pattern.match(self.digit_value)
    
    def _contains_whitespace(self):
        pattern = re.compile("^\s*$")
        return pattern.match(self.digit_value)

    def _validate(self):
        return not self._is_none() and not self._is_empty_string() and \
            not self._contains_whitespace() and self._is_float_number()

    def _validate_hexadecimal(self):
        return not self._is_none() and not self._is_empty_string() and \
            not self._contains_whitespace() and self._is_hexadecimal()

    pass

class DigitType(Enum):
    Binary = 2
    Octal = 8
    Decimal = 10
    Hexadecimal = 16
    pass
