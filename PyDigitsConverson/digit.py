from enum import Enum

class Digit:
    """description of class"""

    _default_separator = '.'
    _invalid_triad = "Invalid triad."
    _invalid_tetrad = "Invalid tetrad."
    _invalid_input_string = "Invalid input string: 1. input string is null or empty; 2. invalid separator."
    _separator_missmatch = "Input string and separator missmatch."

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
    pass

class DigitType(Enum):
    Binary = 2
    Octal = 8
    Decimal = 10
    Hexadecimal = 16
    pass
