from digit import Digit, DigitType

class BinaryDigit(Digit):
    """description of class"""

    def __init__(self, digit_value='0', digit_type=2, separator='.'):
        super().__init__(digit_value=digit_value, digit_type=digit_type, separator=separator) 
        self.separator = separator
        self.digit_type = digit_type
        self.digit_value = digit_value

    def get_decimal(self):
        return self._get_decimal_integer(2) + self.separator + self._get_decimal_fraction(2)

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
        if self.separator in self.digit_value:
            integer, fraction = self.digit_value.split(self.separator)
        else:
            integer = self.digit_value
            fraction = '0'

        integer_part = self.convert_list_to_string_integer(self._get_hexadecimal_integer(integer))
        fraction_part = self.convert_list_to_string_integer(self._get_hexadecimal_fraction(fraction))
        return integer_part + self.separator + fraction_part

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

    def _get_hexadecimal_integer(self, value):
        result =[]
        length = len(value)
        counter = length

        while counter > 0:

            if(counter - 4 >= 0):
                tetrad = value[counter - 4:counter]
            else:
                additional_zeros = ""
                if(counter==3):
                    additional_zeros = "0"
                if(counter==2):
                    additional_zeros = "00"
                if(counter==1):
                    additional_zeros = "000"
                tetrad = additional_zeros + value[0:counter]
            
            result.append(self._get_hexadecimal_for_tetrad(tetrad))
            counter -= 4

        result.reverse()
        return result

    def _get_hexadecimal_fraction(self, value):              

        result =[]
        if value =='0':
            result.append(value)
            return result

        length = len(value)
        counter = 0

        while counter < length:

            if(counter + 4 <= length):
                tetrad = value[counter:counter+4]
            else:
                additional_zeros = ""
                if(length - counter==3):
                    additional_zeros = "0"
                if(length - counter==2):
                    additional_zeros = "00"
                if(length - counter==1):
                    additional_zeros = "000"
                tetrad = value[counter:length] + additional_zeros
            
            result.append(self._get_hexadecimal_for_tetrad(tetrad))
            counter += 4

        return result
        pass

      


