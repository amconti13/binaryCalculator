print( "This program acts like a calculator for binary numbers.\n" )
print( "Please write numbers in two's complement 8-bit form and choose\n "
      + "x, -, *, / as the operators. (Eg: 00000000 + 11111111)" )
#str = raw_input( "Please input operation: ")
str = "00001111 + 11110000"

splitStr = str.split(' ') #Split string by spaces
num1 = splitStr[0]
op = splitStr[1]
num2 = splitStr[2]



print(num1)
print(num2)
print(op)
