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
                "111" : '7',
            }
        return switcher.get(triad, '222')
    pass

class DigitType(Enum):
    Binary = 2
    Octal = 8
    Decimal = 10
    Hexadecimal = 16
    pass
