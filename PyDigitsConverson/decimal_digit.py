from digit import Digit, DigitType

class DecimalDigit(Digit):
    """description of class"""

    def __init__(self, digit_value='0', digit_type=10, separator='.'):
        super().__init__(digit_value=digit_value, digit_type=digit_type, separator=separator) 
        self.separator = separator
        self.digit_type = digit_type
        self.digit_value = digit_value

    def get_decimal(self):
        return self.digit_value 
    pass


