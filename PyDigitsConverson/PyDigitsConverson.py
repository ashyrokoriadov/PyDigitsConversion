from digit import Digit, DigitType
from decimal_digit import DecimalDigit

digit1 = DecimalDigit()
digit1.digit_value = '10'
print(digit1.get_decimal())

digit2 = DecimalDigit(digit_value='12', digit_type=10, separator='.')
print(digit2.get_decimal())
