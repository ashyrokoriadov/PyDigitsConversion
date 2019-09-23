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
        return self._get_value(2)

    def get_octal(self):
        return self._get_value(8)

    def get_hexadecimal(self):

        integer_part_list = self._get_integer(16) 
        integer_part = self._convert_list_to_string_integer_hexadecimal(integer_part_list)

        fraction_part_list = self._get_fraction(16)
        fraction_part = self._convert_list_to_string_fraction_hexadecimal(fraction_part_list)

        return integer_part + self.separator + fraction_part  

    def _get_value(self, digit_type):

        integer_part_list = self._get_integer(digit_type) 
        integer_part = self.convert_list_to_string_integer(integer_part_list)

        fraction_part_list = self._get_fraction(digit_type)
        fraction_part = self.convert_list_to_string_fraction(fraction_part_list)

        return integer_part + self.separator + fraction_part

    def _get_integer(self, digit_type):

        result =[]
        value = self.digit_value.replace(self.separator, Digit._default_separator)
        value = math.trunc(float(value))
        mod = 0
        devidend = value

        mod = devidend % digit_type
        result.append(mod)
        devidend = int(devidend / digit_type)

        while (devidend > digit_type-1):
            mod = devidend % digit_type
            result.append(mod)
            devidend = int(devidend / digit_type)

        if(devidend !=0):
            result.append(devidend)

        result.reverse()
        return result

    def _get_fraction(self, digit_type):

        result =[]

        value = self.digit_value.replace(self.separator, Digit._default_separator)
        value = float(value)
        value = round(value - math.trunc(value), 3)

        intermediary_result = value * digit_type;
        integer_part = math.trunc(intermediary_result);
        fractional_part = intermediary_result - integer_part;
        result.append(integer_part)
        value = fractional_part

        while(round(value,3) !=0):
            intermediary_result = value * digit_type;
            integer_part = math.trunc(intermediary_result);
            fractional_part = intermediary_result - integer_part;
            result.append(integer_part)
            value = fractional_part

        return result           

    def _convert_list_to_string_integer_hexadecimal(self, list):

        result_value = ''
        for item in list:
            if(item > 9):
                item = Digit.get_letter_for_number(self,item)
            result_value = result_value + str(item) 

        return result_value

    def _convert_list_to_string_fraction_hexadecimal(self, list):

        result_value = ''
        counter = 0
        for item in list:

            if(counter == 10):
                break

            if(item > 9):
                item = Digit.get_letter_for_number(self,item)

            result_value = result_value + str(item) 
            counter += 1

        return result_value

    pass


