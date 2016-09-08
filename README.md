# binaryCalculator
You will write a program that acts like a simple calculator for binary numbers. You should read in a string of input that has the format: number operator number. Each of the numbers should be presented in two's complement 8-bit form. So an input string might look like  10011011 + 00110110. You can assume that the user will enter the data in the proper format. 

You do not need to do error checking of the format.   You should divide up the input string into its three parts. You should then determine which operator is being used. The valid operators are +, -, *, and /. Based on the operator you should perform the corresponding mathematical operation on the two numbers after you convert each string of 1's and 0's into its proper corresponding decimal value. Based on the resulting value you can either

display an error message about overflow occurring if the result is too big, or you can you can echo the desired calculation along with the answer you computed after converting it back into two's complement form. 

You should also print an error message if the calculation is supposed to divide by zero. Lastly, you should place this task inside a query loop that asks the user whether or not to continue performing calculations.
