from digit import Digit, DigitType
from decimal_digit import DecimalDigit

digit1 = DecimalDigit()
digit1.digit_value = '12'
print(digit1.get_binary()) #1010

digit2 = DecimalDigit(digit_value='291,725', digit_type=10, separator=',')
print(digit2.get_binary()) #1100
