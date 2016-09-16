# Created by Arianna Conti 9/9/16
import datetime
date = datetime.date.today()

def dec_to_bin(x): #does the same as "{0:08b}".format( x )
    output = []
    for k in range(0, 8):
        output.append(str(x % 2))
        x = int(x / 2)
    return "".join(reversed(output))

print("------------------------------------------------------------------\n"
      + "Arianna Conti\t\t\t\t\t " + str(date)
      + "\nCSCI 3351\t\t\t\t\t Binary Calculator\n"
      + "------------------------------------------------------------------\n"
      + "This program is a calculator for binary numbers.\n")


again = "$n00py"
while again != "x":
    strg = input("\nPlease write numbers in two's complement 8-bit form and"
                 + " choose\nx, -, *, / as the operators. (Eg: 00000000 +"
                 + " 11111111)\nPlease input operation: ")
                 
    # Split string by spaces
    splitStr = strg.split(' ')
    num1 = splitStr[0]
    op = splitStr[1]
    num2 = splitStr[2]
                 
    # string to int
    num1 = int(num1, 2)
    num2 = int(num2, 2)
                 
    # if negative, get value of number from two's compliment binary
    if num1 > 127: num1 = -((0b11111111 - num1) + 1)
    if num2 > 127: num2 = -((0b11111111 - num2) + 1)

    # calculate
    if op == "+":
        x = num1 + num2  # add
    elif op == "-":
        x = num1 - num2  # subtract
    elif op == "*":
        x = num1 * num2  # mutliply
    elif op == "/":
        if num2 == 0:
            x = "Cannot divide by 0"  # undefined
        else:
            x = num1 / num2  # divide
            if isinstance(x, float):
                x = "This program does not output fractional values (Eg: 0.25)."
    else:
        x = "Invalid operator"
    
    # if answer is an int (aka no issues so far)
    if isinstance(x, int):
        #output = []
        if x < -128 or x > 127:  # overflow
            x = "Overflow has occured, cannot calculate."
        elif x < 0:
            x = ((0b11111111 + x) + 1)  # change to two's complement
            #x = dec_to_bin(x)
            x = "Answer: " + str(dec_to_bin(x))
        else:
            x = "Answer: " + str(dec_to_bin(x))

    # output and prompt
    print( x )
    again = input("Enter any key to do another calculation, "
                  + "or enter x to exit.: ")