# Created by Arianna Conti 9/9/16
import datetime
date = datetime.date.today()
print ("------------------------------------------------------------------\n"
       + "Arianna Conti\t\t\t\t\t " + str(date)
       + "\nCSCI 3351\t\t\t\t\t Binary Calculator\n"
       + "------------------------------------------------------------------\n"
       + "This program is a calculator for binary numbers.\n")

again = "$n00py"
while again != "x":
    str = raw_input( "Please write numbers in two's complement 8-bit form and"
                    + " choose\nx, -, *, / as the operators. (Eg: 00000000 +"
                    + " 11111111)\nPlease input operation: ")
    
#Split string by spaces
    splitStr = str.split( ' ' )
    num1 = splitStr[ 0 ]
    op = splitStr[ 1 ]
    num2 = splitStr[ 2 ]

#string to int
    num1 = int( num1, 2 )
    num2 = int( num2, 2 )

#if negative, get value of number from two's compliment binary
    if num1 > 127 : num1 = -(( 0b11111111 - num1 ) + 1 )
    if num2 > 127 : num2 = -(( 0b11111111 - num2 ) + 1 )

#calculate
    if  op == "+": x = num1 + num2 #add
    elif op == "-": x = num1 - num2 #subtract
    elif op == "*": x = num1 * num2 #mutliply
    elif op == "/":
        if num2 == 0: x = "Cannot divide by 0" #undefined
        else: x = num1 / num2 #divide
    else: x = "Invalid operator"

#if answer is an int
    if isinstance( x, int ):
        if x < -128 or x > 127: #overflow
            x = "Overflow has occured, cannot calculate."
        elif x < 0 :
            x = (( 0b11111111 + x ) + 1 )#change to two's complement
            x = "{0:08b}".format( x )#int to binary with 0's instead of 0b
        else:
            x = "{0:08b}".format( x )

#output and prompt
    print("Answer: " + x)
    again = raw_input("Enter any key to do another calculation, "
                      + "or enter x to exit.: ")