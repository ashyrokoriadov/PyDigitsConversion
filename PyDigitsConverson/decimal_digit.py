import math 
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

    def get_binary(self):
        return self._get_binary_integer() + self.separator + self._get_binary_fraction()

    def _get_binary_integer(self):

        result =[]
        value = self.digit_value.replace(self.separator, Digit._default_separator)
        value = math.trunc(float(value))
        mod = 0
        devidend = value

        mod = devidend % 2
        result.append(mod)
        devidend = int(devidend / 2)

        while (devidend > 1):
            mod = devidend % 2
            result.append(mod)
            devidend = int(devidend / 2)

        if(devidend !=0):
            result.append(devidend)

        result.reverse()

        result_value = ''
        for item in result:
            result_value = result_value + str(item) 
        return result_value

    def _get_binary_fraction(self):

        result =[]

        value = self.digit_value.replace(self.separator, Digit._default_separator)
        value = float(value)
        value = round(value - math.trunc(value), 3)

        intermediary_result = value * 2;
        integer_part = math.trunc(intermediary_result);
        fractional_part = intermediary_result - integer_part;
        result.append(integer_part)
        value = fractional_part

        while(round(value,3) !=0):
            intermediary_result = value * 2;
            integer_part = math.trunc(intermediary_result);
            fractional_part = intermediary_result - integer_part;
            result.append(integer_part)
            value = fractional_part

        result_value = ''
        counter = 0
        for item in result:
            if(counter == 10):
                break
            result_value = result_value + str(item) 
            counter += 1
        return result_value
    pass


