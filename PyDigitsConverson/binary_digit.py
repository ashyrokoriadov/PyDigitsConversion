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
        return self._get_decimal_integer() + self.separator + self._get_decimal_fraction()

    def get_binary(self):
        return self.digit_value

    def get_octal(self):
        if self.separator in self.digit_value:
            integer, fraction = self.digit_value.split(self.separator)
        else:
            integer = self.digit_value
            fraction = '0'

        integer_part = self.convert_list_to_string_integer(self._get_octal_integer(integer))
        fraction_part = self.convert_list_to_string_integer(self._get_octal_fraction(fraction))
        return integer_part + self.separator + fraction_part

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

        if separator_position == -1:
            return "0"

        value = value[separator_position+1:]

        length = len(value)
        for item in value:
            sum += int(item) * (2 ** -(i + 1))
            i +=1
        return  str(sum)[2:]

    def _get_octal_integer(self, value):
        result =[]
        length = len(value)
        counter = length

        while counter > 0:

            if(counter - 3 >= 0):
                triad = value[counter - 3:counter]
            else:
                additional_zeros = ""
                if(counter==2):
                    additional_zeros = "0"
                if(counter==1):
                    additional_zeros = "00"
                triad = additional_zeros + value[0:counter]
            
            result.append(self._get_octal_for_triad(triad))
            counter -= 3

        result.reverse()
        return result

    def _get_octal_fraction(self, value):              

        result =[]
        if value =='0':
            result.append(value)
            return result

        length = len(value)
        counter = 0

        while counter < length:

            if(counter + 3 <= length):
                triad = value[counter:counter+3]
            else:
                additional_zeros = ""
                if(length - counter==2):
                    additional_zeros = "0"
                if(length - counter==1):
                    additional_zeros = "00"
                triad = value[counter:length] + additional_zeros
            
            result.append(self._get_octal_for_triad(triad))
            counter += 3

        return result
        pass


      


