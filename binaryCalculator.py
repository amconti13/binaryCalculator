print( "This program acts like a calculator for binary numbers.\n")
again = None
while again != "x":
    print( "Please write numbers in two's complement 8-bit form and choose\n "
          + "x, -, *, / as the operators. (Eg: 00000000 + 11111111)" )
    str = raw_input( "Please input operation: ")
            #just input() does that actual operation in full.
    #str = "00000101 + 000100000"

    splitStr = str.split( ' ' ) #Split string by spaces
    num1 = splitStr[ 0 ]
    op = splitStr[ 1 ]
    num2 = splitStr[ 2 ]

    num1 = int( num1, 2 )#string to int
    num2 = int( num2, 2 )

    if op == "+":
        x = num1 + num2 #add
    elif op == "-":
        x = num1 - num2 #subtract
    elif op == "*":
        x = num1 * num2 #mutliply
    elif op == "/":
        if num2 == 0:
            x = "Can't divide by 0" #undefined
        else:
            x = num1 / num2 #divide
    else:
        x = "Invalid operator"

    if x < -127 or x > 127: #check for overflow
        x =  "Overflow has occured, cannot calculate."

    if isinstance( x, int ):        #if x is of type integer
        x = "{0:08b}".format( x )   #int to binary with 0's instead of 0b

    print(x)

    again = input("Press any key to do another calculation, or press x to "
                  + "exit.: ")