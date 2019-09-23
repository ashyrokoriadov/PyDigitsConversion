from digit import Digit, DigitType
from decimal_digit import DecimalDigit
from binary_digit import BinaryDigit
from octal_digit import OctalDigit
from hexadecimal_digit import HexadecimalDigit

digit1 =  DecimalDigit()
digit1.digit_value = '12'
print(digit1.get_binary()) #1100
print(digit1.get_octal()) #14
print(digit1.get_hexadecimal()) #C

digit2 = DecimalDigit(digit_value='291,725', digit_type=10, separator=',')
print(digit2.get_binary()) #1100
print(digit2.get_octal()) #443.56314631463146314631463146314631463146314631463146
print(digit2.get_hexadecimal()) #123.B99999999

digit3 = BinaryDigit(digit_value='100100011,1011100110', digit_type=2, separator=',')
print('100100011,1011100110 = ' + digit3.get_binary())
print('100100011,1011100110 = ' + digit3.get_decimal())
print('100100011,1011100110 = ' + digit3.get_octal())
print('100100011,1011100110 = ' + digit3.get_hexadecimal())
print('---------------------------')

digit4 = DecimalDigit(digit_value='399.564', digit_type=10, separator=',')
print("399.564 = " + digit4.get_binary()) 
print("399.564 = " + digit4.get_decimal()) 
print("399.564 = " + digit4.get_octal())
print("399.564 = " + digit4.get_hexadecimal()) 
print('---------------------------')

digit5 = BinaryDigit(digit_value='110011111.10010100011', digit_type=2, separator='.')
print('110011111.1001010001 = ' + digit5.get_binary())
print('110011111.1001010001 = ' + digit5.get_decimal())
print('110011111.1001010001 = ' + digit5.get_octal())
print('110011111.1001010001 = ' + digit5.get_hexadecimal())
print('---------------------------')

digit6 = BinaryDigit(digit_value='110011111', digit_type=2, separator='.')
print('110011111 = ' + digit6.get_binary())
print('110011111 = ' + digit6.get_decimal())
print('110011111 = ' + digit6.get_octal())
print('110011111 = ' + digit6.get_hexadecimal())
print('---------------------------')

digit6 = OctalDigit(digit_value='617.44061115645', digit_type=8, separator='.')
print('617.44061115645 = ' + digit6.get_binary())
print('617.44061115645 = ' + digit6.get_decimal())
print('617.44061115645 = ' + digit6.get_octal())
print('617.44061115645 = ' + digit6.get_hexadecimal())
print('---------------------------')

digit6 = HexadecimalDigit(digit_value='18F.90624DD28', digit_type=16, separator='.')
print('18F.90624DD28 = ' + digit6.get_binary())
print('18F.90624DD28 = ' + digit6.get_decimal())
print('18F.90624DD28 = ' + digit6.get_octal())
print('18F.90624DD28 = ' + digit6.get_hexadecimal())
print('---------------------------')